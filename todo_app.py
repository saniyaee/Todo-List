# To-Do List App with Status
# Author: Saniya
todo_list = []
def show_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list,1):
            status = "✔️ Done" if task["done"] else "❌ Pending"
            print(f"{i}.{task['title']}[{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title,"done": False})
    print("Task added!")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 0<num<=len(todo_list):
            todo_list[num-1]["done"] = True
            print("task marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number.")
def remove_task():
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 0<num<=len(todo_list):
            removed = todo_list.pop(num-1)
            print(f"Removed: {removed['title']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number.")

def save_tasks():
    with open("tasks.txt","w") as f:
        for task in todo_list:
            line = f"{task['title']}|{task['done']}\n"
            f.write(line)
    print("Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            for line in f:
                parts = line.strip().split('|')
                title = parts[0]
                done = parts[1] == "True"
                todo_list.append({"title":title,"done": done})
        print("Tasks loaded from tasks.txt")
    except FileNotFoundError:
        print("No saved tasks found.")

# ====== MAIN PROGRAM =====
load_tasks()

while True:
    print("\n===== TO-DO APP MENU =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Save Tasks")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    print(f"You entered: '{choice}'")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
