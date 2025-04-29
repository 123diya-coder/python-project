def display_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nYour To-Do List is empty.")

def to_do_list():
    tasks = []
    print("Welcome to the To-Do List!")
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added!")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    to_do_list()
