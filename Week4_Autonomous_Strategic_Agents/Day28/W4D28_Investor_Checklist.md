\# W4D28 — Investor/Stakeholder Demo Checklist



\## Before the call

\- \[ ] Run `W4D28\_Demo\_Runbook.ps1` (Flowise + tools server up)

\- \[ ] Evidence pack screenshots in `/assets`

\- \[ ] Exported chatflow JSONs attached (Day22, Day23, Day24, Day27)

\- \[ ] README Quickstart verified from clean clone



\## During the call (7–10 min)

\- \[ ] RAG answer with \*\*Sources + Confidence\*\*

\- \[ ] File Search tool demo (answer cites filenames/snippets)

\- \[ ] Scenario run (p05/p50/p95 + hit % + action items)

\- \[ ] “refresh memory” + re-ask to show update



\## Q\&A crib notes

\- \*\*Privacy:\*\* Local-only; no web; controllable ingestion; no secrets.

\- \*\*Defensibility:\*\* Workflow + datasets + prompts + tool wiring; reproducible flows.

\- \*\*Scaling path:\*\* Swap local LLM with hosted; CI to rebuild vector store; auth token checks.

\- \*\*Ops cost:\*\* Free today; future = model/API + vector DB + CI minutes.



\## Risks \& mitigations

\- \*\*Hallucination risk:\*\* Tight Top-K + thresholds; Sources mandatory; “unknown” allowed.

\- \*\*Model latency:\*\* Use smaller local models or hosted for demo; cache embeddings.

\- \*\*Data drift:\*\* “refresh memory” + scheduled re-index in CI.



