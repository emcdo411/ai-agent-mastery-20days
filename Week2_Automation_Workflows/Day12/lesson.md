\# Day 12 — Time-Driven Digest Email from Sheets



\## 📌 Objective

Send yourself a daily HTML email digest of the 10 most recent items captured in `Automation\_Inbox`.



\## 🛠 Steps (≤30 min)



1\. In your `Automation\_Inbox` Google Sheet, open \*\*Extensions → Apps Script\*\*.



2\. \*\*Add this function\*\* (set your email address in the `email` variable):



```javascript

function SendDailyDigest() {

&nbsp; const email = "you@example.com"; // <- change to your email

&nbsp; const ss = SpreadsheetApp.getActive();

&nbsp; const sh = ss.getSheetByName("Sheet1") || ss.getSheets()\[0];



&nbsp; const lastRow = sh.getLastRow();

&nbsp; if (lastRow < 2) return; // no data yet



&nbsp; // Read all rows: Timestamp, Source, Title, URL, Notes, Status

&nbsp; const data = sh.getRange(2, 1, lastRow - 1, 6).getValues();



&nbsp; // Sort newest first by Timestamp (col A = index 0)

&nbsp; data.sort((a, b) => new Date(b\[0]) - new Date(a\[0]));



&nbsp; // Take top 10

&nbsp; const recent = data.slice(0, 10);



&nbsp; // Render HTML rows

&nbsp; const rows = recent.map(r => {

&nbsp;   const ts = Utilities.formatDate(new Date(r\[0]), Session.getScriptTimeZone(), "yyyy-MM-dd HH:mm");

&nbsp;   const title = (r\[2] || "").toString();

&nbsp;   const url = (r\[3] || "").toString();

&nbsp;   const notes = (r\[4] || "").toString();

&nbsp;   const status = (r\[5] || "").toString();

&nbsp;   const linkCell = url ? `<a href="${url}">link</a>` : "";

&nbsp;   return `<tr><td>${ts}</td><td>${title}</td><td>${linkCell}</td><td>${notes}</td><td>${status}</td></tr>`;

&nbsp; }).join("");



&nbsp; const html = `

&nbsp;   <h3>AI Mastery Daily Digest</h3>

&nbsp;   <p>Newest ${recent.length} items from Automation\_Inbox.</p>

&nbsp;   <table border="1" cellpadding="6" cellspacing="0">

&nbsp;     <tr><th>Timestamp</th><th>Title</th><th>URL</th><th>Notes</th><th>Status</th></tr>

&nbsp;     ${rows}

&nbsp;   </table>

&nbsp; `;



&nbsp; MailApp.sendEmail({ to: email, subject: "AI Mastery Digest", htmlBody: html });

}

````



3\. \*\*Authorize \& test\*\*: Click the Run ▶ button for `SendDailyDigest`. Approve permissions. Check your inbox (and spam).



4\. \*\*Schedule it\*\*:



&nbsp;  \* In Apps Script, go to \*\*Triggers\*\* (clock icon) → \*\*Add Trigger\*\*

&nbsp;  \* Choose function: `SendDailyDigest`

&nbsp;  \* Event source: \*\*Time-driven\*\*

&nbsp;  \* Type: \*\*Day timer\*\*

&nbsp;  \* Pick a time (e.g., 7:30 AM)

&nbsp;  \* Save



5\. (Optional) Update your Sheet headers if needed: `Timestamp | Source | Title | URL | Notes | Status`.



\## 📂 Deliverable



Create `Day12\_trigger\_notes.md` with:



\* Recipient email used

\* Scheduled time (timezone)

\* Result of your test run (received email? Y/N)



\## 🎯 Role Relevance



\* \*\*All roles:\*\* A proactive brief in your inbox means faster, better decisions—before meetings, standups, interviews, or investor calls.



````

