\# Day 13 — One-Tap “Process Now” (IFTTT → Webhook → Clean + Digest)



\## 📌 Objective

Trigger your \*\*clean \& digest\*\* pipeline on demand from your phone via an IFTTT Button press.



\## ✅ Prereqs

\- Day 11’s `CleanInbox()` exists in your Apps Script.

\- Day 12’s `SendDailyDigest()` exists and works.



\## 🛠 Steps (≤30 min)



1\. In your `Automation\_Inbox` Google Sheet, open \*\*Extensions → Apps Script\*\*.



2\. \*\*Replace your existing `doPost`\*\* with this version (keeps logging AND supports the `process` action).  

&nbsp;  > If you used `openById("YOUR\_SHEET\_ID")` on Day 9, keep it. Otherwise, `getActive()` works too.



```javascript

function doPost(e) {

&nbsp; try {

&nbsp;   var body = (e \&\& e.postData \&\& e.postData.contents) ? e.postData.contents : "{}";

&nbsp;   var data = {};

&nbsp;   try { data = JSON.parse(body); } catch (err) {}



&nbsp;   // One-tap processing: clean + email digest

&nbsp;   if (data.action === "process") {

&nbsp;     try { CleanInbox(); } catch (err) {}

&nbsp;     try { SendDailyDigest(); } catch (err) {}

&nbsp;     return ContentService.createTextOutput("PROCESSED")

&nbsp;       .setMimeType(ContentService.MimeType.TEXT);

&nbsp;   }



&nbsp;   // Default: log a row coming from IFTTT/Webhooks

&nbsp;   var ss = SpreadsheetApp.getActive(); // or SpreadsheetApp.openById("YOUR\_SHEET\_ID")

&nbsp;   var sh = ss.getSheetByName("Sheet1") || ss.getSheets()\[0];

&nbsp;   sh.appendRow(\[

&nbsp;     new Date(),

&nbsp;     data.source || "IFTTT",

&nbsp;     data.title  || "",

&nbsp;     data.url    || "",

&nbsp;     data.notes  || "",

&nbsp;     data.status || "new"

&nbsp;   ]);

&nbsp;   return ContentService.createTextOutput("OK")

&nbsp;     .setMimeType(ContentService.MimeType.TEXT);



&nbsp; } catch (err) {

&nbsp;   return ContentService.createTextOutput("ERROR: " + err)

&nbsp;     .setMimeType(ContentService.MimeType.TEXT);

&nbsp; }

}

````



3\. \*\*Re-deploy\*\* the Apps Script Web App



&nbsp;  \* \*\*Deploy → Manage deployments → Edit\*\* (or \*\*New deployment\*\*)

&nbsp;  \* Execute as: \*Me\*

&nbsp;  \* Access: \*\*Anyone\*\* (you can tighten later)

&nbsp;  \* Save and copy the \*\*Web App URL\*\*.



4\. \*\*IFTTT\*\* (free): create a Button applet → \*\*Webhooks → Make a web request\*\*



&nbsp;  \* URL: your \*\*Web App URL\*\*

&nbsp;  \* Method: `POST`

&nbsp;  \* Content Type: `application/json`

&nbsp;  \* Body:



```json

{ "action": "process" }

```



5\. \*\*Test\*\*: Press the IFTTT Button.



&nbsp;  \* Sheet should \*\*clean\*\* (duplicates removed, blanks trimmed)

&nbsp;  \* You should receive the \*\*Daily Digest email\*\* (top 10 recent items)



\## 📂 Deliverable



Create `Day13\_end\_to\_end\_checklist.md` with:



\* \[ ] IFTTT Button created

\* \[ ] Web App redeployed (new URL confirmed)

\* \[ ] Button press returns “PROCESSED”

\* \[ ] Sheet cleaned (describe change count)

\* \[ ] Digest email received (time)



\## 🎯 Role Relevance



\* \*\*All roles:\*\* Trigger a meeting-ready intel brief with a single tap before standups, sales calls, interviews, or investor updates.



````



