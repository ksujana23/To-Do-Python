tasks = []

# Create file if it doesn't exist
file = open("tasks.txt", "a")
file.close()

# Load old tasks from file
file = open("tasks.txt", "r")
tasks = file.read().splitlines()
file.close()

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    # View Tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Add Task
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task added successfully!")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))

            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)

                # Update file after deleting
                file = open("tasks.txt", "w")
                for task in tasks:
                    file.write(task + "\n")
                file.close()

                print("Task deleted successfully!")
            else:
                print("Invalid task number")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice")