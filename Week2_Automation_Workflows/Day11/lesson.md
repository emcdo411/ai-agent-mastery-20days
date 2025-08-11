# 🚀 Day 11 — Google Apps Script: Clean & De-Duplicate

## 📌 Objective

Add a **custom menu** to your `Automation_Inbox` Google Sheet that:

* Trims whitespace
* Removes blank rows
* **De-duplicates by URL** (prevents saving the same link twice)

⏱ Target Time: **≤ 30 minutes**

---

## 🛠 Steps

### 1️⃣ Open Apps Script

* In your `Automation_Inbox` Google Sheet → **Extensions → Apps Script**

---

### 2️⃣ Add the Clean & Dedupe Script

Paste the following code **as-is** (works out-of-the-box).

> Assumes Row 1 is your header and the URL is in **Column D**.

```javascript
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("AI Mastery")
    .addItem("Clean Inbox", "CleanInbox")
    .addToUi();
}

function CleanInbox() {
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName("Sheet1") || ss.getSheets()[0];

  // Get all values
  const values = sh.getDataRange().getValues();
  if (values.length < 2) {
    SpreadsheetApp.getUi().alert("No data to clean.");
    return;
  }

  const header = values[0];
  const body = values.slice(1);

  // 1) Trim whitespace & remove blank rows
  const trimmed = body
    .map(row => row.map(c => (typeof c === "string" ? c.trim() : c)))
    .filter(row => row.join("") !== "");

  // 2) Dedupe by URL (column D = index 3)
  const seen = new Set();
  const deduped = [];
  for (const r of trimmed) {
    const url = (r[3] || "").toString().trim();
    const key = url || JSON.stringify(r);
    if (!seen.has(key)) {
      seen.add(key);
      deduped.push(r);
    }
  }

  // Rewrite the sheet
  sh.clearContents();
  sh.getRange(1, 1, 1, header.length).setValues([header]);
  if (deduped.length) {
    sh.getRange(2, 1, deduped.length, deduped[0].length).setValues(deduped);
  }

  SpreadsheetApp.getUi().alert(
    `Clean complete.\nOriginal rows: ${body.length}\nAfter trim/dedupe: ${deduped.length}`
  );
}
```

---

### 3️⃣ Refresh the Sheet

* You should now see a **new menu**: **AI Mastery**.
* Click **AI Mastery → Clean Inbox** to process your sheet.

💡 If your tab isn’t named `"Sheet1"`, either rename it or update `getSheetByName("Sheet1")` to match your tab name.

---

## 📂 Deliverable

Create `Day11_cleanup_log.md` with:

* Rows before vs. after
* Number of blank rows removed
* Number of duplicates removed (from the alert)

---

## 🎯 Role Relevance

**All Roles:** Keeps your automation pipeline **high-signal and clutter-free**, ensuring clean, reliable input data for downstream processes.

---

If you’d like, I can also **add a small diagram** showing how Day 11 (cleaning) feeds into Day 12 (digest) and Day 13 (one-tap trigger) so your readers see the whole flow at a glance.

Do you want me to create that diagram next?



