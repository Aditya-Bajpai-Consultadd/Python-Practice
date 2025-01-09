#Create a program to manage a to-do list with options for 
# adding, updating, removing, and viewing tasks. 
# Use lists and dictionaries to store and manipulate data.

def main():
    tasks = []
    while True:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            update_task(tasks)
        elif choice == 3:
            remove_task(tasks)
        elif choice == 4:
            view_tasks(tasks)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")

def update_task(tasks):
    task = input("Enter task to be updated: ")
    if task in tasks:
        index = tasks.index(task)
        new_task = input("Enter new task: ")
        tasks[index] = new_task
        print("Task updated successfully")
    else:
        print("Task not found")

def remove_task(tasks):
    task = input("Enter task to be removed: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully")
    else:
        print("Task not found")

def view_tasks(tasks):
    for i in tasks:
        print(i)

main()