# Define a function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Define a function to view the to-do list
def view_todo_list(todo_list):
    print("\nTo-Do List:")
    if todo_list:
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

# Define a function to add a task to the to-do list
def add_task(todo_list):
    task = input("\nEnter the task to add: ")
    todo_list.append(task)
    print("Task added successfully.")

# Define a function to mark a task as completed
def mark_completed(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        idx = int(input("\nEnter the index of the task to mark as completed: "))
        if 1 <= idx <= len(todo_list):
            print(f"Marked '{todo_list[idx-1]}' as completed.")
            todo_list.pop(idx-1)
        else:
            print("Invalid index.")
    else:
        print("No tasks to mark as completed.")

# Define a function to delete a task from the to-do list
def delete_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        idx = int(input("\nEnter the index of the task to delete: "))
        if 1 <= idx <= len(todo_list):
            print(f"Deleted '{todo_list[idx-1]}'.")
            todo_list.pop(idx-1)
        else:
            print("Invalid index.")
    else:
        print("No tasks to delete.")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
