<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 13 — Build a Tiny Data App (Databutton for Government & Policy)

## 📌 Objective
- Ship a **useful civic or political micro-tool** (e.g., budget tracker, service backlog estimator).  
- Share a **public app link** that non-technical stakeholders can use.  
- Practice turning raw formulas into **transparent, interactive decision tools**.  

---

## 🛠 Steps (≤45–60 min)

### 1. Choose a Civic Use Case
Instead of ROI for ads, pick a **government or political workflow**:
- **Permit Backlog Estimator**: Inputs = staff_count, avg_time_per_case, backlog_size → Output = days to clear backlog.  
- **Healthcare Clinic Cost Calculator**: Inputs = patients/day, avg_cost_per_patient, subsidy % → Output = monthly cost to government.  
- **Campaign Engagement Forecaster**: Inputs = population_reach, turnout_rate, support_rate → Output = estimated votes.  
- **Disaster Relief Needs Estimator**: Inputs = households_affected, avg_supply_cost, days_of_support → Output = total budget required.  

### 2. Create in Databutton
- App name: e.g., **“Permit Backlog Estimator”**.  
- Define 3 inputs (numeric sliders or text inputs).  
- Define 1 output formula (clear, simple math).  
- Add a **download CSV** button so results can be archived and shared.  

### 3. Publish
- Deploy app in Databutton.  
- Copy the **public URL**.  

### 4. Document
- In `Week2_Vibe_Coding/Day13/databutton_app.md`, include:  
  - **What it does** (plain-language description).  
  - **Inputs/Outputs**.  
  - **Public Link**.  
  - **Next improvement** (e.g., bilingual labels, graphs, add cost scenarios).  

---

## 📂 Deliverables
- Public app URL.  
- `databutton_app.md`.  
- `/logs/day13.md`.  
- Commit:  
  ```bash
  git commit -m "feat(day13): Databutton civic micro-tool + notes"
````

---

## ✅ Rubric (Self-Check)

* [ ] App accepts 3 inputs and returns a meaningful result.
* [ ] Link is public and loads fast.
* [ ] Documentation explains use case in civic/governance terms.
* [ ] One improvement identified for transparency, accessibility, or trust.

---

## 📝 Reflection Prompts (Day 13)

1. What civic/political question did you just make **faster or clearer**?
2. Where would **guardrails** be needed if this tool used real data (privacy, bias, fairness)?
3. What **preset scenarios** would help stakeholders (e.g., “staff cut by 10%,” “turnout rises 5%”)?
4. How might this tool help **municipal leaders in Ethiopia** (budget planning, service delivery, citizen comms)?

---

## 🎯 Role Relevance

* **Policy Analysts:** Turn spreadsheets into **shareable, interactive policy calculators**.
* **Municipal Leaders:** Build transparency tools for **budgeting, permits, healthcare, or disaster response**.
* **Political Campaigns:** Provide **supporters and advisors with live calculators** (turnout, outreach, budget).
* **Governance Teams:** Show citizens clear, simple projections → builds **trust & accountability**.
* **Military Transition / Leadership:** Reinforce mission-style clarity with **inputs → outputs → impact**.

---

✨ **Day 13 Vibe:** You don’t need to be an engineer to ship public-facing data tools. With Databutton, you can turn a **policy question into a transparent app** in under an hour — and share it with stakeholders today.

```

---

Would you like me to also design **3 pre-baked Databutton formulas** (like backlog, budget, turnout) that learners can copy-paste straight into Databutton so they see instant results without overthinking the math?
```



