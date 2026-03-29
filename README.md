# Student Task Ledger

> Your personal, offline-first CLI companion for staying on top of deadlines — without the stress.

---

## Overview

The **Student Task Ledger** is a Python command-line app that gives you one clean, distraction-free place to manage everything on your academic plate. Add tasks, tick them off, sort them by subject, and get an honest look at your productivity — all from your terminal, no internet required.
Juggling assignments, exams, and projects across multiple subjects is hard enough. Keeping track of them shouldn't be.

Your data saves automatically every time, so nothing slips through the cracks.

---

## Features

- **Full Task Management** — Add, view, complete, and delete tasks in just a few keystrokes
- **Smart Categorization** — Organize by subject (e.g., Math, Science) or type (e.g., Exam, Project)
- **Productivity Analytics** — Track your completion rate and see how your workload is distributed across categories
- **Auto-Save** — Data is written to a local JSON file automatically, even if the app closes mid-session
- **Activity Logging** — A background `app_log.txt` quietly records actions and errors for easy debugging
- **Crash-Resistant** — Handles unexpected inputs gracefully so the app never suddenly quits on you

---

## Tech Stack

| Area | Details |
|---|---|
| Language | Python 3.x |
| Data Storage | `json` |
| File Management | `os` |
| Logging | `logging` |
| Timestamps | `datetime` |
| Architecture | Modular Object-Oriented Programming (OOP) |

No external packages needed — runs entirely on Python's built-in standard library.

---

## Getting Started

### Prerequisites

Make sure Python 3 is installed. Open your terminal and run:

```bash
python --version
```

### Setup & Run

1. **Download the project** — grab the source files and drop them into a folder on your computer.

2. **Open your terminal** and navigate to that folder:

```bash
cd path/to/student-task-ledger
```

3. **Launch the app:**

```bash
python main.py
```

No `pip install` needed — you're good to go.

---

## Testing It Out

Run through these quick checks to confirm everything works as expected:

### Test A — Adding a Task
1. Open the app
2. Select **Option 1** → Add Task
3. Fill in the details (e.g., Title: `Math HW`, Date: `2023-12-01`, Category: `Math`)
4. Look for the **"Task added successfully"** message

### Test B — Data Persistence
1. Add a task, then select **Option 6** to exit
2. Relaunch the app (`python main.py`)
3. Select **Option 2** → View Tasks
4. Your task should still be right there waiting

### Test C — Analytics
1. Mark a task complete via **Option 3**
2. Select **Option 5** → View Analytics
3. Confirm the completion rate has updated (e.g., 50% or 100%)

---

## Project Structure

```
.
├── main.py           # Entry point and CLI interface
├── manager.py        # Core task management logic
├── models.py         # Task class definition
├── analytics.py      # Analytics and reporting engine
├── tasks_data.json   # Auto-generated data file (created on first run)
├── app_log.txt       # Auto-generated activity log
├── README.md         # You're reading it
└── statement.md      # Original problem statement
```

---

*Built to bring calm to deadline chaos — one task at a time.*

