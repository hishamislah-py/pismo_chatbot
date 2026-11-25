# Production image: Vite frontend built in stage 1; FastAPI backend + retrieval pipeline + nginx in stage 2.
# The retrieval index (chunks + MiniLM embeddings) is gitignored, so it is built here from the committed knowledge units.
FROM node:22-slim AS web
WORKDIR /web
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 HOME=/root
RUN apt-get update && apt-get install -y --no-install-recommends nginx \
    && rm -rf /var/lib/apt/lists/* /etc/nginx/sites-enabled/default
WORKDIR /app/src
# CPU-only torch keeps the image far smaller than the default CUDA build.
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
COPY backend/requirements.txt backend/requirements.txt
RUN pip install -r backend/requirements.txt sentence-transformers numpy PyYAML openai python-dotenv huggingface_hub
# Embedding model at the exact revision the pipeline loads from ~/.cache/huggingface (scripts/common.py HF_SNAPSHOT).
RUN python -c "from huggingface_hub import snapshot_download; snapshot_download('sentence-transformers/all-MiniLM-L6-v2', revision='1110a243fdf4706b3f48f1d95db1a4f5529b4d41')"
COPY . /app/src
ENV HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
RUN cd pismo_full_corpus_retrieval_experiment \
    && python -B -s scripts/build_corpus.py \
    && python -B -s scripts/embed_corpus.py
COPY --from=web /web/dist /app/web
COPY deploy/nginx.conf /etc/nginx/conf.d/app.conf
EXPOSE 80
CMD ["sh", "/app/src/deploy/start.sh"]
