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

