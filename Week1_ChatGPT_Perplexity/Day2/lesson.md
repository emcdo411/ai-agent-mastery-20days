# Week 1 — Day 2: Structured Prompt Engineering (RTF + PICO with ChatGPT-5)

**Save as:** `week1/day2_structured_prompt_engineering.md`

---

## 🎯 Purpose

Introduce reproducible, structured prompt-engineering techniques that map directly to model evaluation and fine-tuning workflows.
By Day 2, learners will understand how to design **prompt contracts**—inputs and expected outputs that can later feed into LLM evaluation datasets or fine-tuning scripts.

---

## 🧩 Learning Objectives

1. Apply the **RTF** (Role → Task → Format) and **PICO** (Persona · Instructions · Context · Output) frameworks.
2. Build a reusable prompt template that drives consistent, testable results.
3. Evaluate and log differences in reasoning between **ChatGPT-5** and **Perplexity AI**.
4. Save outputs in repo-friendly formats (`.txt`, `.md`) for future model-training data.

---

## ⚙️ Prerequisites (from Day 1)

* Working Python/VS Code/Jupyter environment
* `requirements.txt` installed
* Git repo initialized and synced

---

## 🛠 Agenda (45 min)

|  Time | Segment                                           |
| :---: | :------------------------------------------------ |
|  0–5  | Review RTF + PICO concepts                        |
|  5–15 | Draft your prompt template                        |
| 15–25 | Run and capture outputs (ChatGPT-5 vs Perplexity) |
| 25–35 | Evaluate differences + refine                     |
| 35–45 | Save, log, commit                                 |

---

## 🧠 RTF Formula

**Role → Task → Format**

Example for technical AI prompting:

```
Role: You are an ML engineer designing a regression model for livestock feed efficiency.

Task: Suggest 3 feature-engineering techniques to improve prediction accuracy using real-world agronomic data.  
Include rationale and potential Python libraries.

Format: Return a Markdown table with columns: Technique | Why it helps | Library | Example function
```

---

## 🧭 PICO Framework

| Element      | Purpose                                                                      |
| ------------ | ---------------------------------------------------------------------------- |
| Persona      | Defines authority and tone (e.g., “Senior Data Scientist at a research lab”) |
| Instructions | Explicit steps, criteria, and limitations                                    |
| Context      | Domain, dataset, and environment details                                     |
| Output       | Schema or format to verify against (e.g., JSON, table, markdown)             |

Example:

```
Persona: Senior data scientist working with Microsoft Azure ML.  
Instructions: Evaluate preprocessing methods for predicting cattle feed conversion ratio using probiotics dataset.  
Context: You have structured numeric + categorical features; output needs to be interpretable and reproducible.  
Output: 1) 150-word executive summary; 2) Markdown table (Method | Rationale | Complexity | Expected lift %).
```

---

## 🧮 Prompt Testing Steps

1. Choose a topic (e.g., “Feed-to-Yield Efficiency AI Model Design”).
2. Draft one RTF and one PICO prompt.
3. Run each prompt in ChatGPT-5 and Perplexity.
4. Save outputs as:

   * `Day2_RTF_output.md`
   * `Day2_PICO_output.md`
5. Score each output (1–5) on:

   * Structure matches contract
   * Reasoning clarity
   * Data or reference accuracy
   * Consistency (re-run same prompt)
   * Readability for exec audience
6. Record findings in `logs/day2.md`.

---

## 💾 Deliverables

* `Day2_structured_prompt.txt` → Finalized prompt templates
* `Day2_prompt_comparison.md` → Side-by-side ChatGPT-5 vs Perplexity outputs + comments
* `logs/day2.md` → Reflection + scorecard
* **Commit:** `feat: Day 2 structured prompt engineering (RTF/PICO)`

---

## ✅ Rubric (Self-Check)

| Criterion                             | Pass | Partial | Fail |
| :------------------------------------ | :--: | :-----: | :--: |
| RTF and PICO templates defined        |   ✅  |    ⚠️   |   ❌  |
| Prompt tested in both tools           |   ✅  |    ⚠️   |   ❌  |
| Outputs saved + comparison documented |   ✅  |    ⚠️   |   ❌  |
| Reflection log completed              |   ✅  |    ⚠️   |   ❌  |

---

## 🧾 Reflection Prompts

1. Which tool handled structure and schema best?
2. What did ChatGPT-5 improve over 3.5 (reasoning, formatting, citations)?
3. How could this prompt be repurposed for data labeling or evaluation datasets?
4. What’s one assumption you’d change to improve transferability to a different domain?

---

## 📈 For Your Mentee (Project Extension)

On Day 3, this prompt becomes a **synthetic data generator**—you’ll feed the structured prompts into a Python script that writes JSONL training examples for LLM fine-tuning.

---

