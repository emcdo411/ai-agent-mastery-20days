<!-- Licensed under DACR-1.1 — see LICENSE.md -->

# ⚡ Day 9 — Git Without Fear (Collaboration + Governance Discipline)

## 📌 Objective
- Create/merge a **feature branch** via PR (pull request).  
- Set up a **.gitignore** to protect secrets and reduce noise.  
- Practice **commit hygiene** so your repo reads like an **audit trail**.  
- Build confidence that Git is not scary — it’s your **collaboration + governance backbone**.  

---

## 🛠 Steps (≤30–45 min)

### 1. **Create File**
- Create `Week2_Vibe_Coding/Day11/git_quickstart.md`

### 2. **Paste Quickstart**
```md
# Git Quickstart (5 commands)

git checkout -b feat/home-hero
# edit files…
git add .
git commit -m "feat: hero section + CTA"
git push -u origin feat/home-hero
# open PR → request review → merge to main
````

### 3. **Add .gitignore**

* Create a `.gitignore` file with entries like:

  ```
  node_modules/
  .env
  dist/
  .DS_Store
  logs/
  secrets/
  ```
* This ensures your repo stays clean and **no sensitive files leak**.

### 4. **Make a Change + Open PR**

* Change one line of copy in your site/app.
* Commit with a **specific message**:

  * ✅ Good: `feat: add Amharic translation to About page`
  * ❌ Bad: `update stuff`
* Push → open PR → request review → merge into `main`.

### 5. **Governance Overlay**

* Treat **Git logs as a public record**:

  * Every commit = a decision documented.
  * Every PR = a checkpoint for peer review.
  * `.gitignore` = your **information governance shield**.
* Add PR sections:

  * **Purpose:** Why this change exists.
  * **Impact:** Who/what it affects (citizens, users, stakeholders).
  * **Governance Note:** Does this raise privacy/ethics concerns?

---

## 📂 Deliverables

* `git_quickstart.md` (your notes).
* `.gitignore` file created and committed.
* One merged PR visible in repo history.
* `/logs/day11.md` reflection log.

Commit:

```bash
git commit -m "chore(day11): .gitignore + first PR merged"
```

---

## ✅ Rubric (Self-Check)

* [ ] Branch created & merged via PR.
* [ ] Commit message is **specific and professional**.
* [ ] Secrets and noise excluded via `.gitignore`.
* [ ] Governance overlay added to PR description.

---

## 📝 Reflection Prompts (Day 9)

1. What slowed you down during the PR process?
2. How will you **name branches** going forward (feat/, fix/, chore/)?
3. What belongs in every PR description (purpose, impact, governance note)?
4. How does Git double as a **governance + accountability system** in civic/AI projects?

---

## 🎯 Role Relevance

* **Developers:** Git = your professional hygiene & collaboration foundation.
* **PMs / Policy Leads:** PRs = checkpoints for oversight (transparency in action).
* **Governance Teams:** `.gitignore` = information security baseline.
* **Municipal Leaders (Ethiopia/Caribbean):** See Git as a way to **track every change**, enforce accountability, and build trust.
* **Military Transition:** Git logs mirror **mission logs** — clear, timestamped, auditable.

---

✨ **Day 9 Vibe**: Git isn’t just code control. It’s **civic discipline disguised as tech**. Each commit is a policy note. Each PR is a peer review. Each `.gitignore` is a governance shield.

```

