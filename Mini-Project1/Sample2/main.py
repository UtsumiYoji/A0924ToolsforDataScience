from datetime import datetime


class ToDoApplication:
    PRIORITY_ORDER = {"high": 1, "medium": 2, "low": 3}
    
    # Initialize the list of tasks
    def __init__(self):
        self.tasks = list()
    
    def add_task(self):
        # Get the task, priority, and deadline from the user
        while True:
            input_task = input("Enter the task: ")
            if input_task:
                if input_task in [task["task"] for task in self.tasks]:
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
        self.tasks.append({
            "task": input_task,
            "priority": priority,
            "deadline": deadline
        })
        
        print("'"+input_task+"' with priority '"+priority+"' and deadline '"
            +deadline.strftime("%Y-%m-%d")+"' added successfully.")

    def remove_task(self):
        # Before get input, make sure there is a task
        if not self.tasks:
            print("No tasks to remove.")
            return
        
        while True:
            input_task = input("Enter the task to remove: ")
            if input_task:
                break
            
            print("Task cannot be empty. Please try again.")
            
        # Remove the task
        if input_task not in [task["task"] for task in self.tasks]:
            print("Task not found.")
            return
        
        self.tasks = [task for task in self.tasks if task["task"] != input_task]
        print("'"+input_task+"' has been removed from the list.")
        
    def view_task(self):
        # Before view the task, make sure there is a task
        if not self.tasks:
            print("No tasks to view.")
            return
        
        # View tasks
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            values = list(task.values())
            values[2] = values[2].strftime("%Y-%m-%d")
            print(f"{i+1}.", " - ".join(values))

    def suggest_task(self):
        # Before suggest the task, make sure there is a task
        if not self.tasks:
            print("No tasks to suggest.")
            return
        
        # Sort the tasks by deadline, then priority
        sorted_tasks = sorted(
            self.tasks, key=lambda x: (x["deadline"], self.PRIORITY_ORDER[x["priority"]]))
        
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

    def execute(self):
        while True:
            print("Advanced To-Do List Application")    
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Task")
            print("4. Suggest Task")
            print("5. Exit")
            
            match input("Enter your choice: "):
                case "1":
                    self.add_task()
                case "2":
                    self.remove_task()
                case "3":
                    self.view_task()
                case "4":
                    self.suggest_task()
                case "5":
                    print("Exiting the application. Goodbye!")
                    return
                case _:
                    print("Invalid choice. Please try again.\n")
            
            # Before showing the menu, print a new line
            print()


def main():
    app = ToDoApplication()
    app.execute()

if __name__ == "__main__":
    main()