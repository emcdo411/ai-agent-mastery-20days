# 🚀 Day 28 — Investor Demo, Repo Polish & One-Click Runbook

## 📌 Objective

Deliver an **investor/stakeholder-ready demo** with:

* ✨ A polished, citation-clean repo
* ⚡ A **one-click runbook** to launch server + Flowise + demo
* 📦 An evidence pack + Q\&A crib sheet for pitch confidence

⏳ **Target time:** ≤ 30 minutes

---

## 🎯 Outcomes

* Investor demo flow (**7–10 minutes**)
* One-click script: `W4D28_Demo_Runbook.ps1`
* Evidence pack (`/assets`) with screenshots & JSON
* Investor Q\&A crib sheet

---

## 🛠 Demo Storyline (7–10 min)

1. **Open Flowise** → show **Sources + Confidence** outputs
2. **Ask**: “Week 2 deliverables + validation steps” → highlight file citations
3. **Trigger Tool**: “Find where the daily digest is configured” → File Search → snippet + path
4. **Run Scenario**: “Simulate sales funnel; target revenue 250k, margin 50k” → Day 27 endpoint → p05/p50/p95 + hit %
5. **Show Report**: Day 21 visual brief (trend/histogram)
6. **Prove Trust**: Edit a file → run `refresh memory` → re-ask → show updated answer

---

## ✅ Repo Polish Checklist

* [ ] README: badges, ToC, Mermaid diagram, **Quickstart**, local-data disclaimer
* [ ] `scripts/local_tools_server.py` present; `.venv` auto-creates on run
* [ ] Week folders organized (`WeekX/…`) with JSON, PNG, MD exports
* [ ] Screenshots stored in `/assets` (Flowise, dashboard, Sheet)
* [ ] LICENSE file included (**DACR**)
* [ ] No secrets committed

---

## 📦 Evidence Pack (`/assets`)

* `flowise_chat.png` — RAG answer with Sources/Confidence
* `scenario_reply.png` — JSON → brief summary
* `dashboard_rank.png`, `dashboard_trend.png` — Day 21 visuals
* `sheet_inbox.png` — Week 2 demo
* `make_scenario.png`, `ifttt_applet.png` — automation proof

---

## 🧪 Dry-Run Prompts

Copy/paste for consistency:

```
What are the **Week 2** deliverables and how do I validate each?
Find references to **SendDailyDigest** and **CleanInbox**.
**Simulate** sales funnel; revenue target 250k; margin 50k; 10k trials. Give p05/p50/p95 + hit probabilities.
Summarize **Day 21** outputs for an MBA student with action items.
refresh memory
```

---

## 🛡 Risk, Privacy & Limits (Say Aloud)

* **Local-first** → all tools + models run on localhost, no customer data leaves
* **Citations** → every answer lists file paths; gaps flagged “unknown”
* **Limits** → RAG scope = repo only; web disabled for demo
* **Next** → add API auth, CI rebuild on merge, scaling path to hosted models

---

## 📂 Deliverables (Today)

* `W4D28_Demo_Runbook.ps1` — one-click launcher
* `W4D28_Investor_Checklist.md` — pre-call/during call list
* `W4D28_Pitch_Outline.md` — slides/notes
* *(Optional)* `W4D28_Demo_Script.md` — word-for-word walkthrough

---

## 💻 One-Click Runbook

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day28\W4D28_Demo_Runbook.ps1"
```

Paste the provided script → Save → Run.
It launches:

* Local Tools Server (`uvicorn`)
* Flowise (Docker or Node fallback)
* Health checks + browser tabs (Flowise, server health, GitHub repo)

---

## 📋 Investor / Stakeholder Checklist

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day28\W4D28_Investor_Checklist.md"
```

**Before the Call**

* [ ] Run `W4D28_Demo_Runbook.ps1` (server + Flowise live)
* [ ] `/assets` evidence pack ready
* [ ] Exported chatflow JSONs (Day 22–27)
* [ ] README Quickstart tested from clean clone

**During the Call**

* [ ] RAG demo with Sources + Confidence
* [ ] File Search demo
* [ ] Scenario simulation with JSON → brief → action items
* [ ] `refresh memory` update

**Q\&A crib** → Privacy, Defensibility, Scaling path, Ops cost

---

## 🎤 Optional Pitch Outline

1. Problem → users need deployable AI agents fast
2. Product → 28-day path, Flowise agent, local RAG, citations + confidence
3. Proof → Week 2 automation, Week 3 data agents, Week 4 strategic agent
4. Demo → RAG, File Search, Scenario sim, refresh memory live
5. Moat → playbooks, repo-grounded RAG, DACR license
6. Ask → pilot cohort, intros, budget

---

⚡ This Day 28 plan makes your repo **investor-credible**: one-click run, repeatable storyline, proof artifacts, and risk guardrails.
Perfect closer for your 28-day course.

---

