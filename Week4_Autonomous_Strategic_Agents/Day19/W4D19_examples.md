# 🌍 W4D19 — Example Outputs (Ethiopia-Focused Modules)

**Save as:** `Week4_Autonomous_Strategic_Agents/Day19/W4D19_examples.md`
**Use:** Reference examples for Day 19 strategy modules (SWOT • Porter’s • OKRs). Replace dummies with **real repo evidence** when testing.

---

## 1️⃣ SWOT Example — Oromia Healthcare (2023–2024)

### JSON Output

```json
{
  "sector": "healthcare",
  "region": "Oromia",
  "timeframe": "2023-2024",
  "strengths": [
    { "point": "Expanded rural clinic coverage", "evidence": "Coverage increased by 12% in Oromia clinics", "sources": ["oromia_health_budget_2023.csv"] }
  ],
  "weaknesses": [
    { "point": "Shortage of trained nurses", "evidence": "Nurse-to-patient ratio 1:800 vs national 1:500", "sources": ["oromia_staffing_survey.md"] }
  ],
  "opportunities": [
    { "point": "Donor-funded maternal health programs", "evidence": "World Bank maternal health grant approved", "sources": ["healthcare_donor_notes.md"] }
  ],
  "threats": [
    { "point": "Regional instability affecting logistics", "evidence": "Supply disruptions reported in Q3 2023", "sources": ["logistics_report_oromia.txt"] }
  ],
  "confidence": "Medium",
  "notes": "Some gaps in latest staffing data after July 2023"
}
```

### Executive Brief

* Oromia healthcare shows **strength in rural clinic expansion** but faces **critical nurse shortages**.
* **Donor-backed maternal health funding** is a near-term opportunity.
* **Instability and logistics issues** remain key threats to service delivery.
* **Confidence:** Medium (missing updated July staffing figures).
* **Sources:** `oromia_health_budget_2023.csv`, `oromia_staffing_survey.md`, `healthcare_donor_notes.md`

**Action Items**

1. Prioritize nurse training pipeline.
2. Allocate logistics contingency budget.
3. Leverage maternal health grants for scaling.

---

## 2️⃣ Porter’s Five Forces Example — Addis Ababa Education (2024)

### JSON Output

```json
{
  "sector": "education",
  "region": "Addis Ababa",
  "timeframe": "2024",
  "forces": [
    { "name": "Threat of New Entrants (NGOs/private)", "rating": 3, "rationale": "Private academies increasing enrollment share", "sources": ["education_market_aa.csv"] },
    { "name": "Bargaining Power of Suppliers (teachers)", "rating": 4, "rationale": "High turnover due to low salaries", "sources": ["teacher_attrition_survey.md"] },
    { "name": "Bargaining Power of Citizens", "rating": 2, "rationale": "Limited parent advocacy channels", "sources": ["parent_feedback_notes.md"] },
    { "name": "Threat of Substitutes (alternative providers)", "rating": 2, "rationale": "Few substitutes beyond tutoring", "sources": ["education_trends.txt"] },
    { "name": "Inter-Regional Rivalry", "rating": 3, "rationale": "Competition with Oromia schools for teacher talent", "sources": ["regional_comparison.csv"] }
  ],
  "overall": { "rating": 3, "comment": "Moderately competitive, supplier power (teachers) most critical." },
  "confidence": "High",
  "notes": "Strong survey coverage in 2023–24 dataset."
}
```

### Executive Brief

* Addis Ababa education faces **high teacher bargaining power** and **moderate competition** with neighboring Oromia.
* Parents have **limited advocacy channels**, reducing citizen pressure.
* **Overall pressure:** moderate (3/5).
* **Confidence:** High (surveys cover 2023–24).
* **Sources:** `education_market_aa.csv`, `teacher_attrition_survey.md`, `regional_comparison.csv`

**Action Items**

1. Address teacher salary + retention incentives.
2. Strengthen parent engagement programs.
3. Monitor private academy growth for equity gaps.

---

## 3️⃣ OKR Example — Ethiopia Healthcare (Maternal Health, H1 2025)

### JSON Output

```json
{
  "sector": "healthcare",
  "region": "national",
  "timeframe": "H1 2025",
  "objectives": [
    {
      "objective": "Reduce maternal mortality rate by 20%",
      "key_results": [
        { "kr": "Increase skilled birth attendance", "metric": "% of births attended by skilled staff", "baseline": "64%", "target": "75%", "source_files": ["maternal_health_baseline.csv"] },
        { "kr": "Expand rural maternal clinics", "metric": "Number of functioning rural maternal clinics", "baseline": "145", "target": "200", "source_files": ["clinic_counts_2024.csv"] }
      ],
      "owners": ["Ministry of Health", "Regional Health Bureaus"],
      "risks": ["Staff turnover", "Supply chain delays"],
      "assumptions": ["Donor funding remains stable", "Security allows clinic operations"]
    }
  ],
  "confidence": "Medium",
  "notes": "Targets ambitious; dependent on donor funding."
}
```

### Executive Brief

* Ethiopia’s **H1 2025 maternal health OKRs** target a **20% mortality reduction**.
* **Skilled birth attendance** should increase from 64% → 75%.
* **Rural maternal clinics** must scale from 145 → 200.
* **Risks:** staff turnover and supply chain delays.
* **Confidence:** Medium (donor dependency).
* **Sources:** `maternal_health_baseline.csv`, `clinic_counts_2024.csv`

**Action Items**

1. Secure stable donor funding contracts.
2. Fast-track rural clinic expansion.
3. Develop retention incentives for skilled birth staff.

---

✅ With these examples, learners can see how repo files (`.csv`, `.md`, `.txt`) flow into **structured JSON → concise briefs → action items** for Ethiopian development priorities, aligned to **Day 19**.

