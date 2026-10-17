
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter your task: ")

        if task_name.strip():
            tasks.append({"name": task_name, "completed": False})
            print("Task added successfully!")
        else:
            print("Task name cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i}. {task['name']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            try:
                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Deleted task: {removed['name']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
