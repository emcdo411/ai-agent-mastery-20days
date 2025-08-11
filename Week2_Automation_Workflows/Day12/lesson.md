# 🚀 Day 12 — Automated Daily Digest Email (Apps Script)

## 📌 Objective

Automatically send yourself a **daily HTML email digest** of the latest cleaned entries from your `Automation_Inbox` Google Sheet.

⏱ Target Time: **≤ 30 minutes**

---

## ✅ Prerequisites

* **Day 11:** `CleanInbox()` is set up and working.

---

## 🛠 Steps

### 1️⃣ Add the Daily Digest Function

In your `Automation_Inbox` Google Sheet:

* **Extensions → Apps Script**
* Add this function to your script:

```javascript
function SendDailyDigest() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName("Sheet1") || ss.getSheets()[0];
  var data = sh.getRange(2, 1, sh.getLastRow() - 1, sh.getLastColumn()).getValues();

  // Get the 10 most recent rows
  var recent = data.slice(-10).reverse();

  // Build HTML email body
  var html = "<h2>Daily Intel Digest</h2><table border='1' cellpadding='5' cellspacing='0'>";
  html += "<tr><th>Date</th><th>Source</th><th>Title</th><th>URL</th><th>Notes</th><th>Status</th></tr>";

  recent.forEach(function(row) {
    html += "<tr>";
    html += "<td>" + row[0] + "</td>";
    html += "<td>" + row[1] + "</td>";
    html += "<td>" + row[2] + "</td>";
    html += "<td><a href='" + row[3] + "'>Link</a></td>";
    html += "<td>" + row[4] + "</td>";
    html += "<td>" + row[5] + "</td>";
    html += "</tr>";
  });

  html += "</table>";

  // Send the email
  MailApp.sendEmail({
    to: Session.getActiveUser().getEmail(),
    subject: "Daily Intel Digest",
    htmlBody: html
  });
}
```

---

### 2️⃣ Set Up a Daily Trigger

* In Apps Script → **Triggers** (clock icon in sidebar)
* Click **+ Add Trigger**:

  * Function to run: `SendDailyDigest`
  * Event source: **Time-driven**
  * Type of time-based trigger: **Day timer**
  * Choose a time (e.g., 8:00 AM)

---

### 3️⃣ Test the Digest

* Run `SendDailyDigest()` manually to confirm:

  * Email arrives in your inbox
  * Table shows the most recent **10 entries**

---

## 📂 Deliverable

Create `Day12_digest_test.md` with:

* [ ] Time of trigger set
* [ ] Manual test successful
* [ ] Email received with correct formatting and data

---

## 🎯 Role Relevance

**All Roles:** Keep stakeholders, teammates, or yourself informed with a **zero-cost, auto-updating daily brief** — perfect for:

* Market intel summaries
* Lead tracking updates
* Meeting prep recaps
* Personal productivity logs

---

If you want, I can also add a **Mermaid diagram** showing how Day 12 and Day 13 connect — so your readers instantly see how the *automated* and *one-tap manual* triggers work together in your workflow.

Do you want me to create that diagram next?

