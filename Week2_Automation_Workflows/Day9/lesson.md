# 🚀 Day 9 — IFTTT → Google Sheets via Apps Script Webhook

## 📌 Objective

Create a **zero-cost automation pipeline** where IFTTT triggers a **webhook** → Google Apps Script writes a new row to your Google Sheet.

⏱ Target Time: **≤ 30 minutes**

---

## 🛠 Steps

### 1️⃣ Open & Set Up Apps Script

1. In your `Automation_Inbox` Google Sheet → **Extensions → Apps Script**.
2. Paste the following code, replacing `YOUR_SHEET_ID` with the Sheet ID from your URL:

```javascript
function doPost(e) {
  const data = JSON.parse(e.postData.contents || "{}");
  const ss = SpreadsheetApp.openById("YOUR_SHEET_ID");
  const sh = ss.getSheetByName("Sheet1") || ss.getSheets()[0];
  const now = new Date();

  sh.appendRow([
    now,
    data.source || "IFTTT",
    data.title || "",
    data.url || "",
    data.notes || "",
    data.status || "new"
  ]);

  return ContentService
    .createTextOutput("OK")
    .setMimeType(ContentService.MimeType.TEXT);
}
```

---

### 2️⃣ Deploy as Web App

* **Deploy → New deployment → Web app**

  * **Execute as:** *Me*
  * **Access:** *Anyone* (adjust security later)
* Copy your **Web App URL** — you’ll need this for IFTTT.

---

### 3️⃣ Configure IFTTT (Free Plan)

1. Create a new **Applet**:

   * **If:** Button widget *(or Note / RSS)*
   * **Then:** Webhooks → Make a web request
2. Fill in:

   * **URL:** Your Web App URL
   * **Method:** `POST`
   * **Content Type:** `application/json`
   * **Body:**

```json
{
  "source": "IFTTT Button",
  "title": "Quick Note",
  "url": "",
  "notes": "Captured from phone",
  "status": "new"
}
```

---

### 4️⃣ Test It

Press the IFTTT button → Confirm that a **new row** appears in your Google Sheet.

---

## 📂 Deliverables

* `Day9_webhook_url.txt` → Paste your Web App URL
* `Day9_ifttt_payload.json` → The JSON payload you used

---

## 🎯 Role Relevance

* **Data Analysts** → 1-tap data logging
* **Entrepreneurs** → Mobile lead capture
* **MBA / PMP** → Meeting notes synced instantly
* **Military Transition** → Job prospect tracking on the go

---

### 💻 Commit & Push Your Work

Run this in PowerShell:

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days"
git add "Week2_Automation_Workflows/Day9/lesson.md"
git commit -m "Week 2 Day 9: IFTTT → Apps Script webhook to Google Sheets"
git push
```
