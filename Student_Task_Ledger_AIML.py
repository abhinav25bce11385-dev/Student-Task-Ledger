import json
import os
import logging
from datetime import datetime

# --- NON-FUNCTIONAL REQ: LOGGING & ERROR HANDLING [cite: 41, 43] ---
logging.basicConfig(
    filename='app_log.txt', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- CONSTANTS ---
DB_FILE = "tasks_data.json"

# --- CLASS 1: DATA MODEL (Technical Expectation: proper design [cite: 50]) ---
class Task:
    def __init__(self, title, due_date, category, status="Pending"):
        self.title = title
        self.due_date = due_date
        self.category = category
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['due_date'], data['category'], data['status'])
        task.created_at = data['created_at']
        return task

# --- CLASS 2: PERSISTENCE & LOGIC (Functional Req: CRUD ) ---
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_data()

    def add_task(self, title, due_date, category):
        try:
            new_task = Task(title, due_date, category)
            self.tasks.append(new_task)
            self.save_data()
            logging.info(f"Task added: {title}")
            print("✔ Task added successfully.")
        except Exception as e:
            logging.error(f"Error adding task: {e}")
            print("✖ Error adding task.")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print(f"\n{'ID':<5} {'Title':<20} {'Due Date':<12} {'Status':<10} {'Category':<10}")
        print("-" * 60)
        for idx, task in enumerate(self.tasks):
            print(f"{idx+1:<5} {task.title:<20} {task.due_date:<12} {task.status:<10} {task.category:<10}")

    def mark_complete(self, task_id):
        try:
            if 0 < task_id <= len(self.tasks):
                self.tasks[task_id - 1].status = "Completed"
                self.save_data()
                logging.info(f"Task {task_id} marked complete")
                print("✔ Task updated.")
            else:
                print("✖ Invalid Task ID.")
        except Exception as e:
            logging.error(f"Error completing task: {e}")

    def delete_task(self, task_id):
        try:
            if 0 < task_id <= len(self.tasks):
                removed = self.tasks.pop(task_id - 1)
                self.save_data()
                logging.info(f"Task deleted: {removed.title}")
                print("✔ Task deleted.")
            else:
                print("✖ Invalid Task ID.")
        except Exception as e:
            logging.error(f"Error deleting task: {e}")

    def save_data(self):
        # Non-Functional Req: Reliability (Data persistence) 
        with open(DB_FILE, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def load_data(self):
        if not os.path.exists(DB_FILE):
            return
        try:
            with open(DB_FILE, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            logging.warning("Corrupt data file found. Starting fresh.")
            self.tasks = []

# --- CLASS 3: ANALYTICS MODULE (Functional Req: Reporting/Analytics ) ---
class AnalyticsEngine:
    @staticmethod
    def generate_report(tasks):
        if not tasks:
            print("\nNot enough data for analytics.")
            return
        
        total = len(tasks)
        completed = sum(1 for t in tasks if t.status == "Completed")
        pending = total - completed
        categories = {}
        
        for t in tasks:
            categories[t.category] = categories.get(t.category, 0) + 1
            
        print("\n--- 📊 Productivity Analytics ---")
        print(f"Total Tasks: {total}")
        print(f"Completion Rate: {int((completed/total)*100)}%")
        print(f"Pending Tasks: {pending}")
        print("Breakdown by Category:")
        for cat, count in categories.items():
            print(f"  - {cat}: {count}")

# --- CLASS 4: USER INTERFACE (Functional Req: Workflow [cite: 23]) ---
class CLIInterface:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        while True:
            print("\n=== 🎓 Student Task Manager ===")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Complete")
            print("4. Delete Task")
            print("5. View Analytics")
            print("6. Exit")
            
            choice = input("Enter choice (1-6): ")

            if choice == '1':
                title = input("Title: ")
                date = input("Due Date (YYYY-MM-DD): ")
                cat = input("Category (e.g., Assignment, Exam): ")
                self.manager.add_task(title, date, cat)
            elif choice == '2':
                self.manager.view_tasks()
            elif choice == '3':
                self.manager.view_tasks()
                try:
                    tid = int(input("Enter Task ID to complete: "))
                    self.manager.mark_complete(tid)
                except ValueError:
                    print("Please enter a number.")
            elif choice == '4':
                self.manager.view_tasks()
                try:
                    tid = int(input("Enter Task ID to delete: "))
                    self.manager.delete_task(tid)
                except ValueError:
                    print("Please enter a number.")
            elif choice == '5':
                AnalyticsEngine.generate_report(self.manager.tasks)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = CLIInterface()
    app.run()
