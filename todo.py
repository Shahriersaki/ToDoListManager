import os

def load_tasks():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def add_task(task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def complete_task(index):
    if index < len(tasks):
        print(f"Completed task: {tasks[index]}")
        del tasks[index]
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    global tasks
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(index)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
