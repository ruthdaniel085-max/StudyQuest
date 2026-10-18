# ⚔️ StudyQuest: Gamifying Academic Success

> **"Turn Syllabi into Quests: Gamifying Academic Success, One Task at a Time."**

StudyQuest is an interactive academic tracking web application powered by **Google Gemini AI**. It automatically parses course syllabus PDFs or images and converts dense academic schedules into a dynamic, RPG-style quest log.

---

## 🌟 Key Features

* 🔮 **AI Syllabus Parsing:** Instant processing of syllabus PDFs and images using Google's `gemini-3.8-flash` model.
* ⚔️ **Dynamic XP System:**
  * **100 XP Boss Battles:** High-stakes exams and major midterms.
  * **50 XP Side Quests:** Daily homework, quizzes, and study plan benchmarks.
* 📊 **Interactive Student Dashboard:** Live quest tracking, level progression, confirmation modals, and real-time XP countdown metrics ($\text{Total XP Remaining} = \text{Total Course XP} - \text{Earned XP}$).
* 👨‍🏫 **Teacher Portal Concept:** Overview analytics for instructors to monitor class progression, approve task completions, and nudge students before deadlines.
* 🌙 **Cyber-RPG Dark Mode:** Modern, highly readable UI designed for late-night study sessions.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript (ES6+), FontAwesome
* **Backend:** Python 3, Flask, Flask-CORS
* **AI Processing:** Google Gemini API (`google-genai` SDK / `gemini-3.8-flash`)
* **Storage:** Local file handling & `localStorage` persistence

---

## 🚀 Quickstart Guide

### 1. Prerequisites
Make sure you have Python 3.10+ installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/ruthdaniel085-max/StudyQuest.git](https://github.com/ruthdaniel085-max/StudyQuest.git)
cd StudyQuest
