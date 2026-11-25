#!/bin/sh
# Container entrypoint: apply Alembic migrations (waiting for PostgreSQL), start nginx, run the API.
set -e
cd /app/src
i=0
until alembic -c backend/alembic.ini upgrade head; do
  i=$((i+1)); [ $i -ge 30 ] && { echo "database not reachable"; exit 1; }
  echo "waiting for database..."; sleep 2
done
nginx
exec python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --proxy-headers --forwarded-allow-ips='*'
