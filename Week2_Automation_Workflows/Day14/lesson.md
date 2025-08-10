\# Day 14 — Weekly Review \& Deployment (Automation Playbook)



\## 📌 Objective

Document your Week 2 automation as a \*\*repeatable playbook\*\* and make it portfolio-ready.



\## ✅ What you should have now

\- Day 9: IFTTT → Apps Script webhook to Google Sheets

\- Day 10: Make.com RSS → Google Sheets

\- Day 11: CleanInbox() Apps Script (trim, remove blanks, dedupe by URL)

\- Day 12: SendDailyDigest() daily HTML email

\- Day 13: One-tap “process now” action via IFTTT Button



\## 🛠 Steps (≤30 min)



1\. Create a new file in this folder named `Week2\_Playbook.md` and include the template below.

2\. Add 2–3 screenshots to `/assets` (your Google Sheet, Make.com scenario, and IFTTT applet).

3\. In the playbook, link those images relatively (example: `!\[Make Scenario](../../assets/make\_scenario.png)`).

4\. Proof the flow end-to-end once more using your IFTTT Button.

5\. Commit and push.



---



\## 🧩 Week 2 Playbook Template (copy below into `Week2\_Playbook.md`)

```



\# Week 2 Automation Playbook — Intel Capture → Clean → Daily Digest



\## Outcome



A zero-cost pipeline that captures industry intel or notes → cleans \& de-dupes → emails a daily digest.



\## Architecture



\* Inputs:



&nbsp; \* IFTTT Button / Note → Webhook → Apps Script → Google Sheet

&nbsp; \* Make.com RSS → Google Sheet (scheduled)

\* Processing:



&nbsp; \* Apps Script `CleanInbox()`

\* Output:



&nbsp; \* Apps Script `SendDailyDigest()` (daily HTML email)

&nbsp; \* One-tap “process now” via IFTTT `{ "action":"process" }`



\## Diagram (Mermaid)



```mermaid

flowchart LR

&nbsp; IFTTT\[IFTTT Button/Note] -- POST /webhook --> GAS\[Apps Script doPost]

&nbsp; RSS\[Make.com RSS] -->|Add Row| Sheet\[(Automation\_Inbox)]

&nbsp; GAS -->|Append Row| Sheet

&nbsp; GAS -->|CleanInbox()| Sheet

&nbsp; GAS -->|SendDailyDigest()| Email\[Daily HTML Email]

&nbsp; Click\[One-Tap Process] -->|{action:"process"}| GAS

```



\## Setup Steps (Concise)



1\. Google Sheet `Automation\_Inbox` with columns: Timestamp, Source, Title, URL, Notes, Status

2\. Apps Script:



&nbsp;  \* `doPost(e)` logs rows and handles `action:"process"`

&nbsp;  \* `CleanInbox()` trims, removes blanks, dedupes by URL

&nbsp;  \* `SendDailyDigest()` emails the 10 most recent items

3\. IFTTT Applets:



&nbsp;  \* Button → Webhooks POST `{ "action":"process" }`

&nbsp;  \* Optional: Note → Webhooks (logs text to Sheet)

4\. Make.com:



&nbsp;  \* Scenario: RSS → Google Sheets (Add Row), schedule every 30 minutes

5\. Security Notes:



&nbsp;  \* Web app access set to “Anyone” for demo; restrict to domain/users before production

&nbsp;  \* Consider adding token check in `doPost` for authenticated calls



\## Ops Guide



\* Daily: Check digest email (adjust time in Triggers if needed)

\* One-tap: Press IFTTT Button before meetings to refresh intel

\* Weekly: Run CleanInbox manually if needed; review RSS sources for quality

\* Failure modes:



&nbsp; \* No email? Reauthorize Apps Script and confirm trigger exists

&nbsp; \* No rows? Check Make.com scenario or IFTTT delivery logs

&nbsp; \* Dedupe too aggressive? Confirm URL column/titles are correct



\## Screenshots



\* !\[Sheet](../../assets/sheet\_inbox.png)

\* !\[Make Scenario](../../assets/make\_scenario.png)

\* !\[IFTTT Applet](../../assets/ifttt\_applet.png)



\## Reuse Patterns



\* Swap RSS feed for a different sector or role

\* Replace IFTTT with a mobile form (Google Form → Sheet)

\* Pipe cleaned rows into Slides/Docs for reports



```



\## 📂 Deliverable

\- `Week2\_Playbook.md` completed with your specifics and screenshot links.



\## 🎯 Role Relevance

\- \*\*All roles:\*\* You now own a reusable, documented intel pipeline suitable for demos, portfolios, and stakeholder briefings.

```



---

