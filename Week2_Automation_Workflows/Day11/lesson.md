\# Day 11 — Google Apps Script: Clean \& De-Duplicate



\## 📌 Objective

Add a custom menu to your `Automation\_Inbox` Google Sheet that:

\- Trims whitespace

\- Removes blank rows

\- De-duplicates by \*\*URL\*\* (so you don’t save the same link twice)



\## 🛠 Steps (≤30 min)



1\. In your `Automation\_Inbox` Google Sheet go to \*\*Extensions → Apps Script\*\*.



2\. \*\*Paste this code\*\* (replace nothing yet; it works as-is).  

&nbsp;  > Assumptions: Row 1 is your header. URL is column \*\*D\*\*.



```javascript

function onOpen() {

&nbsp; SpreadsheetApp.getUi()

&nbsp;   .createMenu("AI Mastery")

&nbsp;   .addItem("Clean Inbox", "CleanInbox")

&nbsp;   .addToUi();

}



function CleanInbox() {

&nbsp; const ss = SpreadsheetApp.getActive();

&nbsp; const sh = ss.getSheetByName("Sheet1") || ss.getSheets()\[0];



&nbsp; // Get all values

&nbsp; const values = sh.getDataRange().getValues();

&nbsp; if (values.length < 2) {

&nbsp;   SpreadsheetApp.getUi().alert("No data to clean.");

&nbsp;   return;

&nbsp; }



&nbsp; const header = values\[0];

&nbsp; const body = values.slice(1);



&nbsp; // 1) Trim whitespace on all string cells \& drop totally blank rows

&nbsp; const trimmed = body

&nbsp;   .map(row => row.map(c => (typeof c === "string" ? c.trim() : c)))

&nbsp;   .filter(row => row.join("") !== "");



&nbsp; // 2) Dedupe by URL (column D = index 3)

&nbsp; const seen = new Set();

&nbsp; const deduped = \[];

&nbsp; for (const r of trimmed) {

&nbsp;   const url = (r\[3] || "").toString().trim();

&nbsp;   const key = url || JSON.stringify(r);

&nbsp;   if (!seen.has(key)) {

&nbsp;     seen.add(key);

&nbsp;     deduped.push(r);

&nbsp;   }

&nbsp; }



&nbsp; // Rewrite the sheet

&nbsp; sh.clearContents();

&nbsp; sh.getRange(1, 1, 1, header.length).setValues(\[header]);

&nbsp; if (deduped.length) {

&nbsp;   sh.getRange(2, 1, deduped.length, deduped\[0].length).setValues(deduped);

&nbsp; }



&nbsp; SpreadsheetApp.getUi().alert(

&nbsp;   `Clean complete.\\nOriginal rows: ${body.length}\\nAfter trim/dedupe: ${deduped.length}`

&nbsp; );

}

````



3\. \*\*Refresh\*\* the Sheet; you should see a new menu: \*\*AI Mastery\*\*.

4\. Click \*\*AI Mastery → Clean Inbox\*\* and watch it process.



> ✅ If your tab isn’t named “Sheet1”, either rename the tab to “Sheet1” or change the code line `getSheetByName("Sheet1")` to your tab name.



\## 📂 Deliverable



Create a file in this folder:



\* `Day11\_cleanup\_log.md` with:



&nbsp; \* Rows before vs. after

&nbsp; \* How many blanks removed

&nbsp; \* How many duplicates removed (approx; from the alert)



\## 🎯 Role Relevance



\* \*\*All roles:\*\* Keeps inputs clean so your automation stays high-signal and reliable.



````



