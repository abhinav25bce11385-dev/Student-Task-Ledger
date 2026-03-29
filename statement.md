# Problem Statement & Project Scope

---

## 1. Problem Statement

Students today are dealing with more academic pressure than ever. Between assignments, exams, and back-to-back project deadlines, it's easy for things to fall through the cracks — especially when your only system is a sticky note or a half-forgotten reminder on your phone. This often leads to what most students know all too well: the **"deadline crunch"** — that last-minute panic that comes from losing track of what's due and when.

**The Core Problem:** Students don't have a single, offline-friendly tool that helps them not just *list* what needs to be done, but actually *understand* how they're managing their time — without getting sucked into bloated, internet-dependent apps that create more distraction than they solve.

---

## 2. Scope of the Project

The **Student Task Ledger** is a desktop CLI application that sits comfortably between a basic to-do list and a full-blown project management tool — simple enough to open in seconds, but smart enough to actually help.

The scope includes:

- **Task Lifecycle Management** — Letting students create, update, and delete academic tasks as their workload changes
- **Data Persistence** — Saving everything locally to a JSON file so the app works offline and picks up right where you left off
- **Analytics Engine** — Turning task data into real productivity insights: completion rates, category breakdowns, and study habit patterns
- **System Auditing** — Running a quiet background log of all activity, useful for troubleshooting or reviewing usage over time

---

## 3. Target Users

This tool was built with three kinds of people in mind:

- **University & High School Students** — Managing assignments and deadlines across multiple subjects at once
- **Self-Learners** — Running their own curriculum and wanting a straightforward way to track progress across topics
- **Educators & TAs** — Keeping tabs on grading workloads or admin tasks without needing a complicated system to do it

---

## 4. High-Level Features

- **CRUD Task Operations** — Full control over task entries: create, read, update, and delete
- **Deadline Tracking** — Due date fields that help you see what needs attention first
- **Category Tagging** — Classify tasks by subject (e.g., "Math", "Physics") or type (e.g., "Assignment", "Exam") for a clearer picture of your workload
- **Productivity Analytics** — A reporting module that shows your completion percentage and breaks down tasks by category
- **Automatic Data Preservation** — Data is saved to disk in real time, so nothing is lost if the app closes unexpectedly
- **Error-Resilient Interface** — A menu system that handles typos and invalid inputs without crashing or losing your place
