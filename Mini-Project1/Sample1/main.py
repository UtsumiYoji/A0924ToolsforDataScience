from datetime import datetime

# Initialize the list of tasks
tasks = list()

def add_task():
    # Get the task, priority, and deadline from the user
    while True:
        input_task = input("Enter the task: ")
        if input_task:
            for task in tasks:
                if task["task"] == input_task:
                    print("Task already exists. Please try again.")
                    continue
            break
        
        print("Task cannot be empty. Please try again.")
    
    while True:
        priority = input("Enter the priority (high, medium, low): ")
        if priority in ["high", "medium", "low"]:
            break
        
        print("Invalid priority. Please try again.")
    
    while True:
        deadline = input("Enter the deadline (YYYY-MM-DD):")
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d")
            break
        except:
            print("Invalid deadline. Please try again.")
    
    # Make a dictionary
    tasks.append({
        "task": input_task,
        "priority": priority,
        "deadline": deadline
    })
    
    print("'"+input_task+"' with priority '"+priority+"' and deadline '"
          +deadline.strftime("%Y-%m-%d")+"' added successfully.")

def remove_task():
    # Before get input, make sure there is a task
    if not tasks:
        print("No tasks to remove.")
        return
    
    while True:
        input_task = input("Enter the task to remove: ")
        if input_task:
            break
        
        print("Task cannot be empty. Please try again.")
        
    # Remove the task
    for task in tasks:
        if task["task"] == input_task:
            tasks.remove(task)
            print("'"+input_task+"' has been removed from the list.")
            return
        print("Task not found.")
    
def view_task():
    # Before view the task, make sure there is a task
    if not tasks:
        print("No tasks to view.")
        return
    
    # View tasks
    for i in range(len(tasks)):
        print(
            str(i+1) + ". "
            +tasks[i]["task"] + " - "
            +tasks[i]["priority"] + " - "
            +tasks[i]["deadline"].strftime("%Y-%m-%d")
            )

def suggest_task():
    # Before suggest the task, make sure there is a task
    if not tasks:
        print("No tasks to suggest.")
        return
    
    # Sort the tasks by deadline, then priority
    sorted_tasks = sorted(tasks, key=lambda x: (x["deadline"], x["priority"]))
    
    # Pick up the first 3 tasks
    suggested_tasks = sorted_tasks[:3]
    
    # Suggest the task
    print("Good afternoon! Here are some tasks you might want to work on:")
    for task in suggested_tasks:
        print(
            task["task"] + " - "
            +task["priority"] + " - "
            +task["deadline"].strftime("%Y-%m-%d")
            )

def main():
    while True:
        print("Advanced To-Do List Application")    
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Suggest Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.\n")
            continue
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_task()
        elif choice == "4":
            suggest_task()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            return
        
        # Before showing the menu, print a new line
        print()

if __name__ == "__main__":
    main()