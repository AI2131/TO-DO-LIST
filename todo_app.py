from datetime import datetime
import json
import os


tasks = []

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        tasks = json.load(f)


def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. View Task Stats")
    print("7. Exit")


def add_task():
    title = input("Enter the task title: ")
    task = {
        "title": title,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }
    tasks.append(task)
    save_tasks()
    print("✅ Task added!")


def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for index, task in enumerate(tasks):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{index + 1}. {task['title']} - {status} (Added on {task['created_at']})")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks()
            print("🎉 Task marked as done!")
        else:
            print("❗ Invalid task number.")
    except:
        print("❗ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"🗑 Task '{removed['title']}' deleted.")
        else:
            print("❗ Invalid task number.")
    except:
        print("❗ Please enter a valid number.")


def search_tasks():
    keyword = input("Enter keyword to search: ").lower()
    found = False
    print("\n🔎 Search Results:")
    for index, task in enumerate(tasks):
        if keyword in task["title"].lower():
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{index + 1}. {task['title']} - {status} (Added on {task['created_at']})")
            found = True
    if not found:
        print("🚫 No tasks found matching that keyword.")


def show_stats():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["done"])
    pending_tasks = total_tasks - completed_tasks

    print("\n📊 TASK STATS:")
    print(f"Total Tasks     : {total_tasks}")
    print(f"Completed Tasks : {completed_tasks}")
    print(f"Pending Tasks   : {pending_tasks}")


while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        search_tasks()
    elif choice == "6":
        show_stats()
    elif choice == "7":
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("❗ Invalid choice. Please select from 1 to 7.")
# Save tasks on exit