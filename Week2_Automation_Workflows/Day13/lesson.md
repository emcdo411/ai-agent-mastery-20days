# 🚀 Day 13 — One-Tap “Process Now” (IFTTT → Webhook → Clean + Digest)

## 📌 Objective

Enable a **single-tap trigger from your phone** to run your **Clean + Daily Digest** pipeline instantly using an IFTTT Button.

⏱ Target Time: **≤ 30 minutes**

---

## ✅ Prerequisites

* **Day 11:** `CleanInbox()` exists in your Apps Script.
* **Day 12:** `SendDailyDigest()` exists and works as intended.

---

## 🛠 Steps

### 1️⃣ Update Your Apps Script

In your `Automation_Inbox` Google Sheet:

* **Extensions → Apps Script**
* **Replace your existing `doPost`** with the version below (retains logging + adds `"process"` action).

> If you used `openById("YOUR_SHEET_ID")` in Day 9, keep it. Otherwise `getActive()` works too.

```javascript
function doPost(e) {
  try {
    var body = (e && e.postData && e.postData.contents) ? e.postData.contents : "{}";
    var data = {};
    try { data = JSON.parse(body); } catch (err) {}

    // One-tap processing: clean + email digest
    if (data.action === "process") {
      try { CleanInbox(); } catch (err) {}
      try { SendDailyDigest(); } catch (err) {}
      return ContentService.createTextOutput("PROCESSED")
        .setMimeType(ContentService.MimeType.TEXT);
    }

    // Default: log a row from IFTTT/Webhooks
    var ss = SpreadsheetApp.getActive(); // or openById("YOUR_SHEET_ID")
    var sh = ss.getSheetByName("Sheet1") || ss.getSheets()[0];
    sh.appendRow([
      new Date(),
      data.source || "IFTTT",
      data.title  || "",
      data.url    || "",
      data.notes  || "",
      data.status || "new"
    ]);
    return ContentService.createTextOutput("OK")
      .setMimeType(ContentService.MimeType.TEXT);

  } catch (err) {
    return ContentService.createTextOutput("ERROR: " + err)
      .setMimeType(ContentService.MimeType.TEXT);
  }
}
```

---

### 2️⃣ Redeploy Your Web App

* **Deploy → Manage deployments → Edit** (or **New deployment**)
* **Execute as:** *Me*
* **Access:** *Anyone* (tighten later)
* Save and copy your **Web App URL**.

---

### 3️⃣ Create the IFTTT Button

* **Platform:** IFTTT (Free)
* **If:** Button widget
* **Then:** Webhooks → Make a web request

  * **URL:** Your Web App URL
  * **Method:** `POST`
  * **Content Type:** `application/json`
  * **Body:**

```json
{ "action": "process" }
```

---

### 4️⃣ Test the Flow

Press the IFTTT Button → Expect:

* **Sheet cleaned** → Duplicates removed, blanks trimmed
* **Daily Digest email** → Top 10 recent items delivered

---

## 📂 Deliverable

Create `Day13_end_to_end_checklist.md` with:

* [ ] IFTTT Button created
* [ ] Web App redeployed (new URL confirmed)
* [ ] Button press returns **"PROCESSED"**
* [ ] Sheet cleaned (note change count)
* [ ] Digest email received (timestamp)

---

## 🎯 Role Relevance

**All Roles:** Instantly generate a meeting-ready intel brief before:

* Standups
* Sales calls
* Interviews
* Investor updates

---

If you’d like, I can also create a **flow diagram** for Day 13 that visually maps the one-tap process from your phone to the email arriving — perfect for your GitHub portfolio or README. Would you like me to add that?



