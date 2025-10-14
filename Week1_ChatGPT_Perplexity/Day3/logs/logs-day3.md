# 🧭 Day 3 Log — Synthetic Data Generation & Dual-Model Workflow

**Author:** Erwin Maurice McDonald  
**Program:** AI Model Mastery (Microsoft SWE Track)  
**Date:** YYYY-MM-DD  

---

## 🧠 Summary
Today’s focus was on **bridging structured prompts (Day 2)** and **structured data generation**.  
Using Perplexity for factual grounding and ChatGPT-5 for schema-consistent generation,
we created a synthetic dataset suitable for feed-to-yield model evaluation.

---

## ⚙️ Environment Check
| Component | Version | Status |
|------------|----------|---------|
| Python | 3.11.x | ✅ |
| pandas | 2.x | ✅ |
| plotly | 5.x | ✅ |
| fastapi | 0.111+ | ✅ |
| jsonschema | 4.x | ✅ |
| Validation Script (`test_synthetic_data.py`) | Pass / Fail | ☐ |

---

## 📊 Validation Summary
| Metric | Expected | Observed | Notes |
|:--|:--:|:--:|:--|
| Records Generated | ≥10 | | |
| JSON Schema Pass Rate | 100% | | |
| Avg Feed Conversion Ratio | 6.5–7.5 | | |
| Avg ROI (%) | 10–20 | | |
| Mean Confidence Score | 0.85–0.95 | | |
| Missing Fields Detected | 0 | | |

---

## 🧮 Observations
- ChatGPT-5 produced balanced, domain-consistent data aligned with Perplexity references.  
- ROI and FCR values remained within credible industry ranges.  
- JSON schema validation passed on all lines.  
- Citations followed the expected “Publisher (Year)” pattern.  

---

## 🪶 Reflection Prompts
1. **Data Quality:** Did the synthetic data reflect real-world variation and trends?  
2. **Tool Synergy:** How did Perplexity’s factual scaffolding improve GPT-5’s generation fidelity?  
3. **Reproducibility:** Could you rerun this process tomorrow and get schema-consistent results?  
4. **Governance:** How might this approach help generate training data *without* exposing private datasets?  
5. **Next Iteration:** How can this dataset power Day 4’s Plotly visualization and evaluation metrics?

---

## 🧩 Learning Takeaways
> Example: “Perplexity improved factual context; ChatGPT-5 generated consistent schema-compliant synthetic data.
The workflow established a repeatable pattern for safe dataset creation.”

---

## ✅ Completion Checklist
- [ ] Fact pack created with ≥3 recent, sourced references  
- [ ] Synthetic dataset generated and validated (JSONL)  
- [ ] Executive summary saved  
- [ ] Reflection log completed  
- [ ] Commit pushed to repository  

---

### 💾 Commit Example
```bash
git add Day3_factpack.txt logs/day3.md
git commit -m "chore: Day 3 reflection and validation log"
git push
