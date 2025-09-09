# 🧠 Week 4 — Ethiopia AI Governance Prompt (for W4 RAG Agents)

Use this file as a **drop-in system/user prompt** for your **Week 4 Flowise RAG agents** (W4D16–W4D18). It tells the agent exactly **which files to trust**, how to **summarize budget vs. outcomes**, and how to **cite sources** for auditability.

---

## 📦 Repository Context (Week 4 paths)

> Place or symlink your data into Week 4 so the RAG can find it via your loader globs.

**Required inputs (suggested locations):**

* `Week4_Autonomous_Strategic_Agents/Day16/data/ethiopia_healthcare_budget.csv`
* `Week4_Autonomous_Strategic_Agents/Day16/notes/service_delivery_notes.md`
* `Week4_Autonomous_Strategic_Agents/Day17/data/ethiopia_population_survey.csv`
* `Week4_Autonomous_Strategic_Agents/Day17/notes/ethiopia_population_notes.md`

**If you prefer a shared folder, use:**

* `Week4_Autonomous_Strategic_Agents/_shared/data/ethiopia_healthcare_budget.csv`
* `Week4_Autonomous_Strategic_Agents/_shared/data/ethiopia_population_survey.csv`
* `Week4_Autonomous_Strategic_Agents/_shared/notes/service_delivery_notes.md`
* `Week4_Autonomous_Strategic_Agents/_shared/notes/ethiopia_population_notes.md`

> Make sure your Flowise **Document Loader** includes these paths in its globs (e.g., `Week4_Autonomous_Strategic_Agents/**/*.md, **/*.csv`).

---

## 🎯 Task (What the agent should do)

**Summarize Ethiopia’s** **budget execution vs. service delivery outcomes** for **Healthcare** and **Education** between **2022–2024**—grounded only in the files listed above.

---

## 🧭 Instructions for the Agent (paste into your prompt)

* Compare **budget vs. spent** in `ethiopia_healthcare_budget.csv`.
* Link outcomes to **population survey “% access”** changes from `ethiopia_population_survey.csv`.
* Highlight **regional gaps** (e.g., **Addis Ababa** vs **Oromia**).
* Flag **risks or challenges** from `service_delivery_notes.md` and `ethiopia_population_notes.md`.
* Enforce governance:

  * **Only** use retrieved repo context—**no speculation**.
  * **Cite filenames** (and section if available) in a **Sources** section.
  * If context is insufficient, say **“I don’t have enough context in this repo to answer confidently.”** and ask **one** clarifying question.

**Output format:**

* **Brief Findings** (3–6 bullets)
* **Action Items** (2–4 bullets, e.g., “Expand ICT in Oromia schools”)
* **Confidence** (High | Medium | Low) + **one-line reason**
* **Sources** (file paths; add line refs if feasible)

> Optional localization: add one Amharic line prefixed with **“አጭር ማጠቃለያ:”** at the end.

---

## 🧪 Example Prompts (for Week 4 agents)

1. “Summarize Ethiopia’s **2023 healthcare budget execution in Oromia** and its **impact on access %**.”
2. “What are the **top risks to service delivery** in 2024 based on notes + data?”
3. “Compare **Addis Ababa vs. Oromia** in **education access** — what factors explain the gap?”
4. “Create a **3-point action plan** for Ethiopia’s healthcare sector in 2024, grounded in repo data.”

---

## ✅ Expected Output (sample)

```markdown
### Findings
- Oromia healthcare budget execution improved in 2023 (+~10%) but still trails Addis Ababa’s execution rate.
- Addis Ababa maintains >90% education access; Oromia remains ~15 pts lower, with rural connectivity cited as a constraint.
- Service delivery notes point to staff shortages and ICT gaps as recurring bottlenecks.

### Action Items
- Expand maternal health funding and staffing in Oromia (target primary care centers).
- Launch a rural ICT pilot for schools in Oromia by Q3 2024 with teacher enablement.
- Publish monthly budget dashboards (execution vs. outcomes) for public audit.

### Confidence
**Medium** — Budget execution trends are clear; some 2024 spend fields are incomplete.

### Sources
- Week4_Autonomous_Strategic_Agents/Day16/data/ethiopia_healthcare_budget.csv (lines 6–12)
- Week4_Autonomous_Strategic_Agents/Day17/data/ethiopia_population_survey.csv (lines 3–8)
- Week4_Autonomous_Strategic_Agents/Day16/notes/service_delivery_notes.md
- Week4_Autonomous_Strategic_Agents/Day17/notes/ethiopia_population_notes.md
```

---

## 🔧 Flowise Tips (Week 4)

* **Use with W4D16–W4D18 RAG flows**:

  * **W4D16:** base local RAG setup
  * **W4D17:** multi-tool router (file search / CSV profile / RAG)
  * **W4D18:** refreshable memory + citations guardrails
* **Retriever defaults:** `topK=4–5`, `scoreThreshold=0.35–0.45`, chunks `1000/150`
* Ensure the retriever passes **`metadata.filePath`** (or `source`) so filename citations appear.

---

## 🗂 Deliverable Name (suggested)

Save this file as:
`Week4_Autonomous_Strategic_Agents/Day18/w4_ethio_governance_prompt.md`

> You can also keep a copy in `_shared/prompts/` if multiple Day flows will reuse it.

---

## 🧭 What “Good” Looks Like

* Answers **always** include a **Sources** section with Week 4 file paths.
* Findings and actions are **short, specific, and tied** to CSV + notes evidence.
* The agent **asks a single clarifying question** when data is thin instead of guessing.


