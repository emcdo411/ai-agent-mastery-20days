# 🤖 Day 6 — Domain-Specific Q\&A Bot (ChatGPT-5 Enhanced)

## 📌 Objective

* Build a chatbot prompt restricted to a **single domain** (policy, agriculture, healthcare, disaster response, etc.).
* Train AI to answer **only within scope** and politely reject off-topic queries.
* Leverage **ChatGPT-5’s improved boundary control** for reliability.
* Save transcript, reflect, and commit.

---

## 🛠 Steps (30–45 min)

### 1. Pick Your Domain

Select one that matters to your **country or sector**:

* Caribbean: *Agriculture diversification*, *Tourism risk reduction*, *Hurricane readiness*.
* Ethiopia: *Healthcare staffing*, *Education policy*, *Digital infrastructure*.
* General: *Finance*, *Cybersecurity*, *Project management*.

---

### 2. Write Your Domain-Specific Bot Prompt

Example template:

```markdown
You are a domain expert in [chosen field].  
Only answer questions directly related to this domain.  
If asked something outside scope, reply:  
"⚠️ That is outside my domain expertise."  

Additional rules (ChatGPT-5 advantage):  
- Provide citations when referencing public data or reports.  
- Use Markdown formatting for clarity (headings, bullets, tables).  
- If asked a borderline question, explain why it’s partially relevant or not.  
- Keep answers concise (max 200 words).  
- Offer bilingual output (English + local language) for summaries.
```

---

### 3. Test the Bot

* Ask **3–4 relevant domain questions** (e.g., “What are the biggest threats to cassava exports in 2025?”).
* Ask **1–2 off-topic questions** (e.g., “Who won the World Cup in 2022?”).
* Observe whether ChatGPT-5:

  * Stayed in scope.
  * Used bilingual or structured formatting properly.
  * Applied the “outside expertise” rule correctly.

---

### 4. Save Transcript

* Export and save conversation as:

  * `Day6_domain_bot.md`

---

## 📂 Deliverables

* `Day6_domain_bot.md` — transcript of domain Q\&A + boundary tests.
* `/logs/day6.md` — reflection log.
* Commit with message:

  * `feat: Day 6 domain-specific Q&A bot (ChatGPT5)`

---

## ✅ Rubric (Self-Check)

* [ ] Domain clearly defined.
* [ ] AI stayed in scope for relevant queries.
* [ ] AI rejected off-topic queries gracefully.
* [ ] Used Markdown formatting and optional bilingual output.
* [ ] Reflection log added.
* [ ] Commit pushed with clear message.

---

## 📝 Reflection Prompts (Day 6)

1. **Prompt Effectiveness**

   * Did ChatGPT-5 follow the rules better than you’d expect from 3.5?

2. **Boundary Control**

   * Did the AI politely reject off-topic queries or drift into speculation?

3. **Workflow Fit**

   * Where could a domain-only bot reduce noise (gov FAQs, NGO helpdesks, internal knowledge bases)?

4. **Surprises & Insights**

   * Did the AI handle borderline questions (partially relevant) better than expected?

5. **Next Iteration**

   * Would you add stricter rules (token limits, citation requirements)?
   * Would you add a fallback option (“refer user to human expert”)?

---

## 🎯 Role Relevance

* **Data Pros:** Keeps analysis **laser-focused**.
* **Entrepreneurs:** Creates niche **advisory or customer-support bots**.
* **Analysts:** Sharpens **domain mastery** without distractions.
* **MBA/PMP:** Enables **subject-focused prep** (finance, policy, ops).
* **Military Transition:** Builds MOS-aligned knowledge bots with **ChatGPT-5’s improved scope discipline**.

---

