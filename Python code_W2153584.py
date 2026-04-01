import os
from datetime import datetime  

# List to store tasks
tasks = []

# File name for saving the tasks
TASK_FILE = "test1.txt"

# Function to load tasks from a file
def load_tasks_from_file():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                name, description, priority, due_date = line.strip().split("|")
                task = {
                    "name": name,
                    "description": description,
                    "priority": priority,
                    "due_date": due_date
                }
                tasks.append(task)
    else:
        print("Task not found!")

#Function to save tasks to a file
def save_tasks_to_file():
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['description']}|{task['priority']}|{task['due_date']}\n")

#Function to add a new task
def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter priority (High, Medium, Low): ")
    
# Validate to due date 
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d") 
            break
        except ValueError:
            print("Invalid format! Use YYYY-MM-DD.")

    task = {"name": name, "description": description, "priority": priority, "due_date": due_date}
    tasks.append(task)
    save_tasks_to_file()
    print(f"Task '{name}' added successfully!")

#Function to update the task
def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            task['name'] = input(f"Enter new name ({task['name']}): ") or task['name']
            task['description'] = input(f"Enter new description ({task['description']}): ") or task['description']
            task['priority'] = input(f"Enter new priority ({task['priority']}): ") or task['priority']

# Validate new due date input
            while True:
                new_due_date = input(f"Enter new due date ({task['due_date']}): ") or task['due_date']
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    task['due_date'] = new_due_date
                    break
                except ValueError:
                    print("Invalid format! Use YYYY-MM-DD.")

            save_tasks_to_file()
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

#Function to view all tasks
def view_tasks():
    if not tasks:
        print("Task not found!")
        return
    print("Task List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Name: {task['name']}, Description: {task['description']}, "
              f"Priority: {task['priority']}, Due Date: {task['due_date']}")

#Function to delete a task
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks_to_file()
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

# Main program
def main():
    load_tasks_from_file()
    
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number.")

# Run the main program
if __name__ == "__main__":
    main()

