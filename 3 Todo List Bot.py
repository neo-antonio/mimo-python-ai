print()
print("Hi, welcome to your todo list bot! Select an option below to start.")
print()

todo_list = []

while True:
    print("\nTO DO LIST:")
    if not todo_list:
        print("You have no tasks in your to-do list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

    print("\nOPTIONS:")
    print("1 - Add a task")
    print("2 - Remove a task")
    print("3 - Quit the program")
    print()

    choice = input("Enter a number: ")

    if choice == "1":
        new_task = input("Enter task name: ")
        todo_list.append(new_task)
        print(f'\nSuccessfully added "{new_task}" to your to-do list!')

    elif choice == "2":
        if not todo_list:
            print("\nYou have no tasks in your to-do list.")
        else:
            print("\nTO DO LIST:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            
            try:
                remove_task = int(input("\nSelect a task number to remove: "))
                if 1 <= remove_task <= len(todo_list):
                    removed_task = todo_list.pop(remove_task - 1)
                    print(f'\nSuccessfully removed "{removed_task}"!')
                else:
                    print("\nInvalid task number. Please try again.")
            except ValueError:
                print("\nPlease enter a valid number.")

    elif choice == "3":
        print("\nExiting program...")
        break

    else:
        print("\nUnrecognized command. Please try again.")
