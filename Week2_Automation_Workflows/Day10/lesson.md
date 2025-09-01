<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 10 — How Software Gets Built (End-to-End)

## 📌 Objective
- Document a **lightweight SDLC** for this week’s build.
- Publish a **visual flow** + mini backlog.

---

## 🛠 Steps (≤30 min)

1. **Create**
   - `Week2_Vibe_Coding/Day10/build_flow.md`

2. **Paste diagram**
   ```mermaid
   flowchart LR
     A[Idea<br/>PRD] --> B[Plan<br/>issues]
     B --> C[Build<br/>feature branch]
     C --> D[Test<br/>unit + manual]
     D --> E[Review<br/>PR + approvals]
     E --> F[Merge<br/>main]
     F --> G[Deploy<br/>preview/prod]
     G --> H[Monitor<br/>metrics/logs]
     H --> I[Iterate<br/>next issues]

📂 Deliverables

build_flow.md + backlog list

/logs/day10.md

Commit: docs(day10): build flow + mini backlog

✅ Rubric (Self-Check)

 Flow includes review + deploy + monitor

 Backlog ties to PRD user stories

 Only this week’s essentials included

📝 Reflection Prompts (Day 10)

Where will quality most likely break?

What can you skip now and add later?

What’s your rollback plan?
