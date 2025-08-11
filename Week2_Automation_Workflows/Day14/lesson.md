Here’s your **modernized Day 14 lesson markdown** — more readable, visually engaging, and portfolio-ready while keeping all your original structure intact.

---

# 🚀 Day 14 — Weekly Review & Deployment (Automation Playbook)

## 📌 Objective

Transform your **Week 2 automation** into a **repeatable, documented playbook** that’s polished enough for your portfolio or stakeholder demos.

⏱ Target Time: **≤ 30 minutes**

---

## ✅ By Now, You Should Have

* **Day 9:** IFTTT → Apps Script Webhook → Google Sheets
* **Day 10:** Make.com RSS → Google Sheets
* **Day 11:** `CleanInbox()` Apps Script (trim, remove blanks, dedupe by URL)
* **Day 12:** `SendDailyDigest()` Daily HTML Email
* **Day 13:** One-tap “Process Now” Action via IFTTT Button

---

## 🛠 Steps

1️⃣ **Create the Playbook File**

* In this folder, add a file named:

  ```
  Week2_Playbook.md
  ```

2️⃣ **Add Screenshots**

* Place 2–3 images into `/assets` showing:

  * Your Google Sheet (`Automation_Inbox`)
  * Your Make.com Scenario
  * Your IFTTT Applet

3️⃣ **Link Images in Playbook**

* Use relative links:

  ```markdown
  ![Make Scenario](../../assets/make_scenario.png)
  ```

4️⃣ **Proof the Flow**

* Trigger your IFTTT Button → Verify data flows from capture → clean → digest email.

5️⃣ **Commit & Push**

* Save your changes to Git.

---

## 🧩 Week 2 Automation Playbook Template

Copy this into `Week2_Playbook.md` and replace placeholders with your specifics:

````markdown
# Week 2 Automation Playbook — Intel Capture → Clean → Daily Digest

## Outcome  
A zero-cost pipeline that:
- Captures industry intel or notes  
- Cleans & deduplicates entries  
- Delivers a daily HTML digest email  

## Architecture  
* **Inputs:**  
  - IFTTT Button/Note → Webhook → Apps Script → Google Sheet  
  - Make.com RSS → Google Sheet (scheduled)  

* **Processing:**  
  - Apps Script `CleanInbox()`  

* **Outputs:**  
  - Apps Script `SendDailyDigest()` (daily HTML email)  
  - One-tap “process now” via IFTTT `{ "action":"process" }`  

## Diagram (Mermaid)
```mermaid
flowchart LR
  IFTTT[IFTTT Button/Note] -- POST /webhook --> GAS[Apps Script doPost]
  RSS[Make.com RSS] -->|Add Row| Sheet[(Automation_Inbox)]
  GAS -->|Append Row| Sheet
  GAS -->|CleanInbox()| Sheet
  GAS -->|SendDailyDigest()| Email[Daily HTML Email]
  Click[One-Tap Process] -->|{action:"process"}| GAS
````

## Setup Steps (Concise)

1. Google Sheet `Automation_Inbox` with columns: Timestamp, Source, Title, URL, Notes, Status
2. Apps Script:

   * `doPost(e)` → Logs rows & handles `action:"process"`
   * `CleanInbox()` → Trims, removes blanks, dedupes by URL
   * `SendDailyDigest()` → Emails 10 most recent items
3. IFTTT Applets:

   * Button → Webhooks POST `{ "action":"process" }`
   * Optional: Note → Webhooks (logs text to Sheet)
4. Make.com:

   * RSS → Google Sheets (Add Row), scheduled every 30 min
5. Security:

   * Web app set to “Anyone” for demo (restrict before production)
   * Optionally add token check in `doPost` for authentication

## Ops Guide

* **Daily:** Check digest email (adjust trigger times as needed)
* **One-Tap:** Press IFTTT Button pre-meeting to refresh intel
* **Weekly:** Manually run `CleanInbox()`; review RSS sources for quality

**Failure Modes:**

* No email? → Reauthorize Apps Script & verify trigger exists
* No rows? → Check Make.com scenario or IFTTT delivery logs
* Dedupe issues? → Confirm URL & title columns are correct

## Screenshots

* ![Sheet](../../assets/sheet_inbox.png)
* ![Make Scenario](../../assets/make_scenario.png)
* ![IFTTT Applet](../../assets/ifttt_applet.png)

## Reuse Patterns

* Swap RSS feed to another industry/role
* Replace IFTTT with Google Forms → Sheets
* Push cleaned rows into Google Slides/Docs for reports

```

---

## 📂 Deliverable  
- `Week2_Playbook.md` filled with **your actual configs, screenshots, and links**  

---

## 🎯 Role Relevance  
- **All Roles:** You now have a **documented, reusable intel pipeline** ready for portfolio demos, client pitches, or stakeholder briefings.  

---

If you want, I can **also produce a one-page "portfolio showcase" layout** for this playbook so it instantly impresses when a recruiter or stakeholder clicks it. That would make this even stronger for your GitHub.
```

