\# Day 9 — IFTTT → Google Sheets via Apps Script Webhook



\## 📌 Objective

Build a zero-cost pipeline: IFTTT triggers a \*\*webhook\*\* → Apps Script writes a row to your Sheet.



\## 🛠 Steps (≤30 min)

1\. Open your `Automation\_Inbox` Sheet → \*\*Extensions → Apps Script\*\*.

2\. Paste this code and replace `YOUR\_SHEET\_ID` with your Sheet ID (from the URL):



```javascript

function doPost(e) {

&nbsp; const data = JSON.parse(e.postData.contents || "{}");

&nbsp; const ss = SpreadsheetApp.openById("YOUR\_SHEET\_ID");

&nbsp; const sh = ss.getSheetByName("Sheet1") || ss.getSheets()\[0];

&nbsp; const now = new Date();

&nbsp; sh.appendRow(\[

&nbsp;   now,

&nbsp;   data.source || "IFTTT",

&nbsp;   data.title || "",

&nbsp;   data.url || "",

&nbsp;   data.notes || "",

&nbsp;   data.status || "new"

&nbsp; ]);

&nbsp; return ContentService.createTextOutput("OK").setMimeType(ContentService.MimeType.TEXT);

}

````



3\. \*\*Deploy\*\* → New deployment → \*\*Web app\*\*



&nbsp;  \* Execute as: \*Me\*

&nbsp;  \* Access: \*\*Anyone\*\* (tighten later)

&nbsp;  \* Copy the \*\*Web App URL\*\*



4\. \*\*IFTTT\*\* (free): Create an Applet



&nbsp;  \* \*\*If:\*\* Button widget (or Note / RSS)

&nbsp;  \* \*\*Then:\*\* Webhooks → Make a web request



&nbsp;    \* URL: your Web App URL

&nbsp;    \* Method: `POST`

&nbsp;    \* Content Type: `application/json`

&nbsp;    \* Body:



```json

{ "source":"IFTTT Button", "title":"Quick Note", "url":"", "notes":"Captured from phone", "status":"new" }

```



5\. Press the button → confirm a new row appears in your Sheet.



\## 📂 Deliverable



\* `Day9\_webhook\_url.txt` (paste your Web App URL)

\* `Day9\_ifttt\_payload.json` (the JSON you used)



\## 🎯 Role Relevance



\* \*\*Data/Analysts:\*\* 1-tap source logging

\* \*\*Entrepreneurs:\*\* Mobile lead capture

\* \*\*MBA/PMP:\*\* Meeting notes to Sheet

\* \*\*Military Transition:\*\* Job prospect notes on the go



````



\### 2) Commit and push (run this in PowerShell)

```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days"

git add "Week2\_Automation\_Workflows/Day9/lesson.md"

git commit -m "Week 2 Day 9: IFTTT → Apps Script webhook to Google Sheets"

git push

````

