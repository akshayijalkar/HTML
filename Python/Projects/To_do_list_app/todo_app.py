# Define a function to display the menu options for the user.
def show_menu_options():
    print("\nTo-Do List Menu:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

# Define a function to view all tasks in the to-do list.
def display_tasks(task_list):
    # Check if the list is empty and notify the user.
    if not task_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        # Loop through the list and display each task with its index.
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Define a function to add a new task to the to-do list.
def add_task(task_list):
    # Ask the user for the task to add.
    new_task = input("Enter the task you want to add: ")
    # Append the task to the list and confirm the addition.
    task_list.append(new_task)
    print(f"'{new_task}' has been added to your to-do list.")

# Define a function to remove a task from the to-do list.
def remove_task(task_list):
    # Display the tasks for the user to choose from.
    display_tasks(task_list)
    # Check if the list is empty before proceeding.
    if task_list:
        try:
            # Ask the user for the task number to remove.
            task_number = int(input("Enter the task number to remove: "))
            # Remove the selected task and confirm the removal.
            removed_task = task_list.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        except (IndexError, ValueError):
            # Handle invalid input or out-of-range task numbers.
            print("Invalid task number. Please try again.")

# Define a function to save tasks to a file.
def save_tasks(task_list):
    # Specify the file name to save the tasks.
    file_name = "tasks.txt"
    # Open the file in write mode and save each task on a new line.
    with open(file_name, "w") as file:
        for task in task_list:
            file.write(task + "\n")
    print(f"Tasks have been saved to '{file_name}'.")

# Define a function to load tasks from a file.
def load_tasks():
    # Specify the file name to load tasks from.
    file_name = "tasks.txt"
    # Initialize an empty list to hold the loaded tasks.
    loaded_tasks = []
    try:
        # Open the file in read mode and load tasks into the list.
        with open(file_name, "r") as file:
            loaded_tasks = [line.strip() for line in file]
        print(f"Tasks have been loaded from '{file_name}'.")
    except FileNotFoundError:
        # Handle the case where the file does not exist.
        print(f"No saved tasks found in '{file_name}'. Starting with an empty to-do list.")
    return loaded_tasks

# Main function to run the To-Do List App.
def run_to_do_list_app():
    # Initialize an empty list to store tasks.
    current_tasks = []
    
    # Load tasks from the file at the start of the program.
    current_tasks = load_tasks()

    # Start a loop to display the menu and handle user choices.
    while True:
        # Display the menu options to the user.
        show_menu_options()
        
        # Prompt the user for their choice.
        user_choice = input("Enter your choice (1-6): ")
        
        # Handle each menu option using if-else conditions.
        if user_choice == "1":
            display_tasks(current_tasks)  # View tasks
        elif user_choice == "2":
            add_task(current_tasks)  # Add a task
        elif user_choice == "3":
            remove_task(current_tasks)  # Remove a task
        elif user_choice == "4":
            save_tasks(current_tasks)  # Save tasks to file
        elif user_choice == "5":
            current_tasks = load_tasks()  # Load tasks from file
        elif user_choice == "6":
            print("Goodbye! Thanks for using the To-Do List App.")
            break  # Exit the loop and program
        else:
            # Handle invalid menu choices.
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the To-Do List App.
run_to_do_list_app()
