# 🚀 Day 10 — Make.com Scenario: RSS → Google Sheets

## 📌 Objective

Set up a **Make.com** (free tier) automation that ingests an RSS feed and automatically appends new entries to your `Automation_Inbox` Google Sheet.

⏱ Target Time: **≤ 30 minutes**

---

## 🛠 Steps

### 1️⃣ Sign In to Make.com

* Go to [make.com](https://www.make.com)
* Create a free account or sign in

---

### 2️⃣ Create Your Scenario

* **Module 1:** **RSS → Watch RSS Feed Items**

  * **Feed URL:** Choose a high-signal feed for your field (e.g., major industry blog, trusted news source)

* **Module 2:** **Google Sheets → Add a Row**

  * Connect your Google account when prompted
  * **Spreadsheet:** `Automation_Inbox`
  * **Sheet/Tab:** Default or your chosen tab
  * **Map Fields:**

    * `Timestamp` → `now`
    * `Source` → `RSS`
    * `Title` → RSS item title
    * `URL` → RSS item link
    * `Notes` → blank or short note
    * `Status` → `new`

---

### 3️⃣ Test the Scenario

* Click **Run once** in Make.com
* Confirm a new row appears in your Google Sheet

---

### 4️⃣ Schedule the Scenario

* Turn **Scheduling ON**
* Suggested interval: **Every 30 minutes** (adjust as needed)

---

## 📂 Deliverable

Create `Day10_scenario_notes.md` with:

* RSS Feed URL used
* Sheet/Tab name
* Schedule interval
* One sentence on *why this feed matters* to you

---

## 🎯 Role Relevance

* **Data Analysts:** Continuous intel stream for trend analysis
* **Entrepreneurs:** Ongoing market/competitor updates
* **MBA / PMP:** Evidence stream for decks & status briefs
* **Military Transition:** Industry news for target roles

---

### 💻 Commit & Push

Run in PowerShell:

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days"
git add "Week2_Automation_Workflows/Day10/lesson.md"
git commit -m "Week 2 Day 10: Make.com RSS → Google Sheets scenario"
git push
```

*(Optional)* Create the deliverable placeholder now:

```powershell
ni -Type File "Week2_Automation_Workflows/Day10/Day10_scenario_notes.md" -Force | Out-Null
git add "Week2_Automation_Workflows/Day10/Day10_scenario_notes.md"
git commit -m "Week 2 Day 10: add scenario notes placeholder"
git push
```

---

If you want, I can also create a **Day 9 → Day 10 mini-workflow diagram** to visually show how IFTTT and RSS feed capture feed into the same Google Sheet. That would make your Week 2 documentation pop in your GitHub.

Do you want me to make that diagram next?

