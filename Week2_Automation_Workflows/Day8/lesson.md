# ⚡ Day 8 — How Software Gets Built (End-to-End + Governance Lens)

## 🎯 Purpose

Day 8 connects **context engineering** to the **real-world build process**.
You’ll visualize how code moves from idea → deployment and where **AI governance checkpoints** protect quality, ethics, and compliance.

By the end, you’ll understand:

* Where each **AI agent** (research, summarization, localization, visualization) plugs into the SDLC.
* How **governance overlays** (policy, ethics, compliance) intersect with engineering stages.
* How to express that flow in Markdown + Mermaid + backlog form.

---

## 📌 Objectives

* Document a **lightweight SDLC** (Software Development Life Cycle).
* Add an **AI-Governance overlay** for review/approval points.
* Draft a **mini backlog** connecting policy and engineering.
* Prepare to link this flow into your future Week 2 dashboard agent.

---

## 🛠 Agenda (30 – 45 min)

|  Time | Task                                                        |
| :---: | :---------------------------------------------------------- |
|  0–10 | Create diagram (`build_flow.md`)                            |
| 10–25 | Add governance overlay nodes (policy + ethics + compliance) |
| 25–35 | Write 3–4 backlog items tied to governance user stories     |
| 35–45 | Save + reflect + commit                                     |

---

## 🧩 Create

```bash
mkdir -p wk02/day08
touch wk02/day08/build_flow.md
```

---

## 🧠 Paste into `build_flow.md`

````markdown
# 🔧 How Software Gets Built (End-to-End + Governance Lens)

```mermaid
flowchart LR
  A[Idea / PRD] --> B[Plan / Issues]
  B --> C[Build / Feature Branch]
  C --> D[Test / Unit + Manual]
  D --> E[Review / PR + Approvals]
  E --> F[Merge / Main]
  F --> G[Deploy / Preview → Prod]
  G --> H[Monitor / Metrics + Logs]
  H --> I[Iterate / Next Issues]

  %% Governance Overlay
  A --> A1[Policy Alignment / Stakeholder Review]
  D --> D1[Ethics + Bias Scan]
  E --> E1[Security + Privacy Approval]
  G --> G1[Risk + Compliance Sign-Off]
````

### 🗂 Governance Backlog (Examples)

* [ ] Add AI Ethics Checklist to Test Stage (D1)
* [ ] Require Security Sign-Off for Major Deployments (E1 → G1)
* [ ] Integrate Bias Scanner into CI/CD Pipeline (D)
* [ ] Draft Policy Alignment Template for All New PRDs (A1)
* [ ] Publish “Decision Log” schema for audit trail (G1)

---

## 📂 Deliverables

* `wk02/day08/build_flow.md` (with Mermaid diagram + backlog)
* `/logs/day8.md` — reflection log (3 bullets on insights)

Commit:

```bash
git add wk02/day08
git commit -m "docs(day8): end-to-end build flow + governance overlay"
```

---

## ✅ Rubric (Self-Check)

| Criterion                                                 | Met? |
| :-------------------------------------------------------- | :--: |
| Flow includes Plan → Deploy → Monitor                     |  ☑️  |
| Governance overlay visible (policy / ethics / compliance) |  ☑️  |
| Backlog ties to policy or governance stories              |  ☑️  |
| Mermaid diagram renders cleanly (GitHub safe syntax)      |  ☑️  |
| Reflection log added                                      |  ☑️  |

---

## 📝 Reflection Prompts (Day 8)

1. Where does **quality** usually break in your pipeline?
2. Which stage needs a **leadership review** most urgently?
3. If you had to **automate one governance gate**, which would it be and why?
4. How do you balance **speed vs oversight** in AI-assisted builds?
5. What would a “citizen impact check” look like in your context?

---

## 🎯 Role Relevance

| Audience                  | Value                                                             |
| :------------------------ | :---------------------------------------------------------------- |
| **Technical Leads / PMs** | See where AI and governance intersect in SDLC.                    |
| **Policy / Ethics Teams** | Learn how to embed review points without blocking engineering.    |
| **Municipal Leaders**     | Understand software accountability in plain language.             |
| **Executives**            | Gain a bird’s-eye view of how compliance and innovation co-exist. |

---

## 🔄 Next in Week 2

Day 9 will convert this **build flow** into a **live dashboard agent** that visualizes progress, flags governance gates, and tracks policy alignment in real time.

---
