import json
import os
import sys
from types import SimpleNamespace

import pytest

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FakeCompletions:
    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        out = self.outputs.pop(0) if len(self.outputs) > 1 else self.outputs[0]
        if isinstance(out, BaseException):
            raise out
        if isinstance(out, SimpleNamespace):
            return out
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=out))])


class FakeClient:
    """Stands in for openai.OpenAI: client.chat.completions.create(...)."""

    def __init__(self, *outputs):
        self.chat = SimpleNamespace(completions=FakeCompletions(outputs))

    @property
    def calls(self):
        return self.chat.completions.calls


def model_json(status="answered", answer="Answer [E1].", citations=("E1",), missing=""):
    return json.dumps({"status": status, "answer": answer, "citations": list(citations), "missing_information": missing})


@pytest.fixture(scope="session")
def retriever():
    from pismo_assistant.retrieval import HybridRetriever
    return HybridRetriever()


@pytest.fixture(scope="session")
def assistant_evidence(retriever):
    """Assistant with the real retriever; generator replaced per test."""
    from pismo_assistant.pipeline import Assistant
    from pismo_assistant.generation import OpenAIGenerator
    return Assistant(retriever=retriever, generator=OpenAIGenerator(client=FakeClient(model_json()), model="fake-model"))
