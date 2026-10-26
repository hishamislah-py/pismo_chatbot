"""Question -> retrieval -> evidence assembly -> OpenAI generation -> citation validation -> response dict.
Each stage is injectable so it can be tested on its own."""
from dataclasses import asdict

from . import citations, config, integrations
from .evidence import OperationIndex, assemble, matched_operations
from .generation import GenerationError, OpenAIGenerator


class Assistant:
    def __init__(self, retriever=None, generator=None, op_index=None, top_k=config.TOP_K):
        if retriever is None:
            from .retrieval import HybridRetriever
            retriever = HybridRetriever()
        self.retriever = retriever
        self.op_index = op_index or OperationIndex(retriever.chunks)
        self.generator = generator or OpenAIGenerator()
        self.top_k = top_k

    def evidence(self, question):
        excluded = integrations.excluded_integrations(question)
        if not excluded:
            return assemble(self.retriever.search(question, k=self.top_k), self.op_index, question=question)
        # client-webhook question: chunks of the other integration are skipped and replaced from the same ranking,
        # and no expansion may add them back
        def exclude(chunk):
            return integrations.chunk_integration(chunk) in excluded
        hits = [h for h in self.retriever.search(question, k=self.top_k + config.SCOPE_OVERFETCH) if not exclude(h.chunk)]
        return assemble(hits[:self.top_k], self.op_index, question=question, exclude=exclude)

    def answer(self, question, generate=True):
        result = {"question": question, "status": None, "answer": "", "citations": [], "warnings": [], "error": None,
                  "evidence": [], "matched_operations": [], "verification": None}
        ev = self.evidence(question)
        result["evidence"] = [{k: v for k, v in asdict(e).items() if k != "text"} | {"chars": len(e.text)} for e in ev]
        result["matched_operations"] = matched_operations(question, self.op_index)
        if not ev:
            result["status"] = "no_evidence"
            result["answer"] = "No knowledge-unit passages were retrieved for this question, so it cannot be answered from the knowledge base."
            return result
        if not generate:
            result["status"] = "evidence_only"
            return result
        try:
            gen = self.generator.generate(question, ev)
        except GenerationError as e:
            result["status"] = "generation_error"
            result["error"] = {"kind": e.kind, "message": e.message}
            return result
        rep = citations.validate(gen.answer, gen.citations, ev, result["matched_operations"], gen.status,
                                 known_identifiers=self.op_index.ops.keys(),
                                 excluded_integrations=integrations.excluded_integrations(question), question=question)
        result.update(status=gen.status, answer=gen.answer, model=gen.model, missing_information=gen.missing_information,
                      citations=citations.sources_for(rep.valid, ev))
        w = result["warnings"]
        if rep.unknown:
            w.append(f"answer cites labels that were not supplied: {rep.unknown}")
        if rep.missing_metadata:
            w.append(f"cited evidence lacks source metadata: {rep.missing_metadata}")
        if rep.unsupported_tokens:
            w.append(f"API details not found in the passages cited by the same claim: {rep.unsupported_tokens}")
        if rep.uncited_claims:
            w.append(f"claims with API details but no citation: {rep.uncited_claims}")
        if rep.operation_mismatch:
            w.append(f"answer does not name the operation the question identified: {rep.operation_mismatch}")
        if rep.cross_operation_claims:
            w.append(f"requirement stated for several operations but not documented for each: {rep.cross_operation_claims}")
        if rep.integration_mismatch:
            w.append(f"claims cite documentation of another integration than the question asks about: {rep.integration_mismatch}")
        if rep.unmarked_historical:
            w.append(f"claims supported only by historical changelog passages are not marked as historical: {rep.unmarked_historical}")
        if rep.uncited_answer and gen.status != "not_documented":
            w.append("answer contains no inline citations")
        result["citations_valid"] = rep.ok
        result["verification"] = rep.checks()
        return result
