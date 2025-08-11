# W4D28 — Investor / Stakeholder Demo Checklist

## ✅ Pre-Call Setup

* [ ] **Run Demo Script** — `W4D28_Demo_Runbook.ps1` (launch Flowise + tools server)
* [ ] **Evidence Pack** — Latest screenshots saved to `/assets`
* [ ] **Chatflows Ready** — Export JSONs for Day22, Day23, Day24, Day27
* [ ] **README Validation** — Quickstart works from a clean clone

---

## 🎯 Live Demo Flow (7–10 min)

1. **RAG Query** — Answer includes **Sources + Confidence Score**
2. **File Search Tool** — Show filename/snippet citations
3. **Scenario Run** — Present p05 / p50 / p95 outcomes + hit % + action items
4. **Memory Refresh** — Re-ask after “refresh memory” to show updated context

---

## 💡 Q\&A Talking Points

* **Privacy** — Local-only execution; no internet dependency; controlled ingestion; no sensitive data
* **Defensibility** — Full workflow transparency (datasets, prompts, tool wiring); reproducible flows
* **Scaling Path** — Swap local LLM for hosted; CI pipeline to rebuild vector store; authentication token checks
* **Operational Cost** — Free now; future = model/API usage + vector DB storage + CI minutes

---

## ⚠️ Risks & Mitigations

* **Hallucination Risk** — Tight Top-K retrieval, source requirement, and “unknown” fallback allowed
* **Model Latency** — Use smaller local models or hosted instances for speed; cache embeddings
* **Data Drift** — Regular “refresh memory” and scheduled re-indexing via CI

---

If you want, I can also **add iconography, bold emphasis, and timing cues** so it reads like a **VC-ready demo script** rather than a checklist.
That would make it flow naturally for your investor call.



