# Week 1 — Day 1: Environment Setup & Readiness for AI Model Engineering

**Save as:** `week1/day1_environment_setup.md`

---

## 🎯 Purpose

Establish a reproducible, professional-grade local development environment that mirrors the workflow of Microsoft Software Engineers and Data Scientists.

---

## 🧩 Learning Objectives

1. Configure a clean **Python + VS Code + GitHub** workspace.
2. Understand the **toolchain** used throughout the program (Jupyter, FastAPI, Azure ML SDK, Plotly).
3. Create a **version-controlled project structure** and connect it to a remote repository.
4. Validate installations and run a simple model sanity test.

---

## 🧠 Why It Matters

At Microsoft scale, reproducibility and governance begin on Day 1. A well-structured environment means:

* fewer dependency conflicts
* seamless collaboration
* faster onboarding to Azure ML and DevOps pipelines
* instant credibility in interviews and peer reviews

---

## ⚙️ Setup Checklist

| Step  | Task                                                                          | Validation                                                                      |
| ----- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **1** | Install **Python 3.11+**                                                      | `python --version` shows ≥ 3.11                                                 |
| **2** | Install **VS Code** + Extensions *(Python, Jupyter, GitHub Copilot optional)* | Open VS Code → Extensions tab → installed                                       |
| **3** | Install **Git**                                                               | `git --version`                                                                 |
| **4** | Create a **GitHub account** (if new)                                          | Can `git clone` and `git push`                                                  |
| **5** | Clone this repo                                                               | `git clone https://github.com/<username>/ai-model-mastery`                      |
| **6** | Create and activate a virtual environment                                     | `python -m venv venv` → `source venv/bin/activate` or `.\venv\Scripts\activate` |
| **7** | Install dependencies                                                          | `pip install -r requirements.txt`                                               |
| **8** | Test FastAPI + Jupyter + Plotly install                                       | Run `python test_setup.py` or open `test_notebook.ipynb` and execute first cell |

---

## 🧰 Core Tools & Libraries

| Category                    | Tools                                  |
| --------------------------- | -------------------------------------- |
| **Core Language**           | Python 3.11                            |
| **Environment**             | VS Code / Jupyter Lab                  |
| **Data Science**            | pandas · NumPy · scikit-learn          |
| **Modeling (optional GPU)** | PyTorch · TensorFlow                   |
| **APIs & Integration**      | FastAPI · Uvicorn                      |
| **Visualization**           | Plotly · Matplotlib · Seaborn          |
| **Cloud/DevOps**            | Azure ML SDK · Docker · GitHub Actions |

---

## 🗂️ Project Structure

```plaintext
ai-model-mastery/
│
├── week1_data_and_basics/
│   ├── day1_environment_setup.md
│   ├── 01_test_environment.ipynb
│   └── README.md
│
├── requirements.txt
├── .gitignore
├── test_setup.py
└── README.md
```

---

## 🧪 Validation Script (example)

```python
# test_setup.py
import sklearn, torch, fastapi, plotly
print("✅ Environment OK")
print("scikit-learn:", sklearn.__version__)
print("PyTorch:", torch.__version__)
print("FastAPI:", fastapi.__version__)
```

Run:

```bash
python test_setup.py
```

Expected output → all versions print successfully.

---

## 📘 Reflection Questions

1. Did your environment reproduce cleanly on another machine?
2. What assumptions about dependencies could cause failure?
3. How could you containerize this for a team?
4. What’s your comfort level with Git branching and pull requests (1-5)?

---

## 🧭 Deliverables

* Screenshot of successful environment test (`✅ Environment OK`)
* GitHub commit: `feat: Day 1 environment setup`
* Updated `reflections.md` (answers + issues faced)

---

## ✅ QA & Acceptance

* [ ] Python 3.11+ installed
* [ ] Virtual environment created & activated
* [ ] Required packages installed
* [ ] Repo successfully cloned & committed
* [ ] Test script executed without error

---

## 🧱 Next Up — Day 2

**Topic:** *Data Loading & Exploration*
You’ll import your first dataset (e.g., Feed-to-Yield Efficiency), handle missing values, and produce your initial exploratory plots in Plotly Studio.

---
