# W4D28 — Investor / Stakeholder Demo Checklist (VC-Ready)

## ✅ Pre-Call Setup (5 min)

* [ ] **Run Demo Script** → `W4D28_Demo_Runbook.ps1` (launch Flowise + tools server)
* [ ] **Evidence Pack** → `/assets` has latest screenshots (Flowise UI, scenario reply, dashboard charts, inbox demo)
* [ ] **Chatflows Ready** → Export JSONs: Day22, Day23, Day24, Day27
* [ ] **README Check** → Quickstart verified on a clean clone

---

## 🎯 Live Demo Flow (7–10 min total)

**0:00–1:30** → **RAG Query**

* Ask: *“What are the Week 2 deliverables and how do I validate each?”*
* Show output → includes **Sources + Confidence Score**

**1:30–3:00** → **File Search Tool**

* Query: *“Find where the daily digest is configured.”*
* Show snippet + filepath citation

**3:00–6:00** → **Scenario Run (Day 27)**

* Ask: *“Simulate sales funnel; target revenue 250k, margin 50k; 10k trials.”*
* Show p05 / p50 / p95 values, hit % for targets, and **2–3 action items**

**6:00–7:30** → **Memory Refresh**

* Edit file → run *“refresh memory”*
* Re-ask earlier question → demo updated context

---

## 💡 Q\&A Talking Points (Have Ready)

* **Privacy** → Local-first; no internet dependency; ingestion controlled; no customer data leaves machine
* **Defensibility** → Full transparency: datasets, prompts, wiring all reproducible
* **Scaling Path** → Hosted LLM swap, CI rebuilds vector store on merge, API auth tokens
* **Operational Cost** → Free now; future = API/model cost + vector DB + CI/CD minutes

---

## ⚠️ Risks & Mitigations (Say Aloud)

* **Hallucination Risk** → Tight Top-K, source requirement, “unknown” fallback
* **Model Latency** → Use smaller local models or hosted LLM; embedding cache for speed
* **Data Drift** → “Refresh memory” on demand; scheduled CI re-index

---

⚡ With this structure, your demo runs like a **7–10 min investor pitch**, not just a repo walkthrough.
The timing cues keep you on track, the talking points build trust, and the risk slide proves foresight.

---




