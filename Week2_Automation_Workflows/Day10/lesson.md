# ⚡ Enhanced Day 8 — How Software Gets Built (End-to-End + Governance Lens)

````markdown
<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 10 — How Software Gets Built (End-to-End + Governance Lens)

## 📌 Objective
- Document a **lightweight SDLC** (software development life cycle).  
- Add an **AI governance overlay** showing where leaders, regulators, or boards should review or approve.  
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

     %% Governance overlay
     A --> A1[Policy Alignment<br/>Stakeholder Review]
     D --> D1[Ethics Check<br/>Bias Scan]
     G --> G1[Risk + Compliance Signoff]
````

3. **Draft mini backlog**

   * List 3–4 backlog items tied to a “governance-aware PRD”
     Example:

     * [ ] Draft privacy checklist for new chatbot.
     * [ ] Add audit log feature.
     * [ ] Create fallback plan for outage.

---

## 📂 Deliverables

* `Week2_Vibe_Coding/Day10/build_flow.md`
* Mini backlog list
* `/logs/day10.md`

Commit: `docs(day10): build flow + mini backlog with governance overlay`

---

## ✅ Rubric (Self-Check)

* [ ] Flow includes **review, deploy, monitor**.
* [ ] Backlog ties to **policy or governance user stories**.
* [ ] Governance checkpoints visible (policy, ethics, compliance).

---

## 📝 Reflection Prompts (Day 10)

1. Where will **quality** most likely break?
2. Where should **leadership/governance reviews** happen?
3. What’s your **rollback plan** if deployment introduces risk?
4. How do you balance **speed vs. oversight**?

---

## 🎯 Role Relevance

* **Political Leaders:** See where **policy review fits inside tech projects**.
* **Municipal Managers:** Learn how to demand checkpoints without coding.
* **AI Governance Teams:** Insert **bias scans, ethics reviews, compliance gates**.
* **Non-Experts:** Understand the “black box” of software in plain workflows.

```

Do you want me to go ahead and **draft the entire Week 2 plan (Days 8–14)** in this same advanced Vibe Coding style so you can see the arc before we refine each day?
```

