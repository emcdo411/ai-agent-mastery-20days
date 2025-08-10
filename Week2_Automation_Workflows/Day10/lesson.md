\# Day 10 — Make.com Scenario: RSS → Google Sheets



\## 📌 Objective

Use \*\*Make.com\*\* (free tier) to ingest an RSS feed and automatically append entries to your `Automation\_Inbox` Google Sheet.



\## 🛠 Steps (≤30 min)

1\. \*\*Sign in\*\* to https://www.make.com (free account).

2\. \*\*Create a Scenario\*\*:

&nbsp;  - \*\*Module 1:\*\* RSS → \*Watch RSS feed items\*

&nbsp;    - Feed URL: choose a high-signal feed for your field (e.g., a major industry blog or news site).

&nbsp;  - \*\*Module 2:\*\* Google Sheets → \*Add a Row\*

&nbsp;    - Connect Google account when prompted.

&nbsp;    - Spreadsheet: `Automation\_Inbox`

&nbsp;    - Sheet/Tab: default (or select your tab)

&nbsp;    - Map fields:

&nbsp;      - `Timestamp` = `now`

&nbsp;      - `Source` = `RSS`

&nbsp;      - `Title` = RSS item title

&nbsp;      - `URL` = RSS item link

&nbsp;      - `Notes` = leave blank or short note

&nbsp;      - `Status` = `new`

3\. \*\*Run once\*\* in Make to test the scenario and confirm a row appears in your Sheet.

4\. \*\*Schedule\*\* the scenario:

&nbsp;  - Turn scheduling \*\*ON\*\*

&nbsp;  - Suggested interval: every \*\*30 minutes\*\* (or as needed).



\## 📂 Deliverable

Create `Day10\_scenario\_notes.md` in this folder with:

\- Feed URL you used

\- Sheet/tab name

\- Schedule interval

\- One sentence on \*why this feed matters\* for you



\## 🎯 Role Relevance

\- \*\*Data Pros / Analysts:\*\* Continuous intel stream for trend analysis  

\- \*\*Entrepreneurs:\*\* Market/competitor updates  

\- \*\*MBA/PMP:\*\* Evidence stream for decks and status briefs  

\- \*\*Military Transition:\*\* Industry news for target roles

```



---



\### 3) Commit and push



```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days"

git add "Week2\_Automation\_Workflows/Day10/lesson.md"

git commit -m "Week 2 Day 10: Make.com RSS → Google Sheets scenario"

git push

```



(Optional) create the deliverable placeholder so it shows up now:



```powershell

ni -Type File "Week2\_Automation\_Workflows/Day10/Day10\_scenario\_notes.md" -Force | Out-Null

git add "Week2\_Automation\_Workflows/Day10/Day10\_scenario\_notes.md"

git commit -m "Week 2 Day 10: add scenario notes placeholder"

git push

```

