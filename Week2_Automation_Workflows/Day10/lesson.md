# 🎶 Day 10 — Vibe Coding with Make.com: *RSS → Google Sheets*

## 🌟 Vibe Objective

Spin up a **hands-off intel pipeline**: every time a blog drops or a feed updates, your Google Sheet catches it automatically like a digital net. You stay in the flow — no copy/paste, no FOMO.

⏱ Target Vibe: **≤ 30 minutes** (coffee break project)

---

## 🌀 Vibe Steps

### 1️⃣ Enter the Make.com Matrix

* Go to [make.com](https://www.make.com)
* Sign in (free tier is all you need to start)

---

### 2️⃣ Build the Scenario (Your Digital Conductor 🎼)

**Module 1: RSS → Watch RSS Feed Items**

* Drop in the feed URL that matters most to you:

  * Tech blogs if you’re an analyst
  * Market news if you’re an entrepreneur
  * Defense or healthcare feeds if you’re transitioning out of the military

**Module 2: Google Sheets → Add a Row**

* Connect your Google account
* Point it to your `Automation_Inbox` sheet
* Map your vibe fields:

  | Sheet Column | Data Flow                      |
  | ------------ | ------------------------------ |
  | `Timestamp`  | `now()`                        |
  | `Source`     | `RSS`                          |
  | `Title`      | RSS item title                 |
  | `URL`        | RSS item link                  |
  | `Notes`      | leave blank or add a quick tag |
  | `Status`     | `new`                          |

---
flowchart LR
    subgraph Day9[Day 9: IFTTT → Google Sheets]
        A[IFTTT Trigger] --> B[Webhook]
        B --> C[Google Sheets: Automation_Inbox]
    end

    subgraph Day10[Day 10: RSS → Google Sheets]
        D[RSS Feed Watcher] --> E[Make.com Scenario]
        E --> C
    end

    C[(Automation_Inbox Sheet)]
    style C fill:#000000,stroke:#ffffff,stroke-width:2px
    style A fill:#f4a261,stroke:#fff,stroke-width:2px
    style B fill:#2a9d8f,stroke:#fff,stroke-width:2px
    style D fill:#e76f51,stroke:#fff,stroke-width:2px
    style E fill:#264653,stroke:#fff,stroke-width:2px

### 3️⃣ Test Your Groove

* Hit **Run once**
* Watch your Google Sheet catch the new row in real-time

---

### 4️⃣ Put It on Autopilot ✈️

* Flip **Scheduling ON**
* Suggested vibe: every **30 minutes** (but you control the beat)

---

## 📂 Mini-Deliverable

Log it with style in `Day10_scenario_notes.md`:

* Feed URL you chose
* Sheet/tab name
* Update interval
* *One-liner on why this feed matters to YOU*

---

## 🎯 Why This Hits Different

* **Analysts:** Continuous data drip for spotting patterns
* **Entrepreneurs:** Competitive radar always on
* **MBA / PMPs:** Evidence stream for decks & updates
* **Veterans in Transition:** Stay sharp with industry news for target roles

---

## 💻 Commit the Energy

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days"
git add "Week2_Automation_Workflows/Day10/lesson.md"
git commit -m "Day 10 vibes: RSS → Google Sheets pipeline"
git push
```

*(Optional placeholder)*

```powershell
ni -Type File "Week2_Automation_Workflows/Day10/Day10_scenario_notes.md" -Force | Out-Null
git add "Week2_Automation_Workflows/Day10/Day10_scenario_notes.md"
git commit -m "Day 10 vibes: add notes placeholder"
git push
```

---

## 🖼 Bonus Vibe

Want me to sketch a **Day 9 → Day 10 vibe map** (IFTTT + RSS both flowing into Google Sheets) as a single diagram? It would show your stack tightening up — perfect for GitHub and demo-worthy for NPower.

---

