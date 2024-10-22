from threading import Timer
from plyer import notification

tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
    reminder_choice = input("Do you want to set a reminder for this task? (yes/no): ").lower()

    if reminder_choice == 'yes':
        try:
            reminder_minutes = int(input("Set a reminder after how many minutes?: "))
            reminder_time = reminder_minutes * 60  
            print(f"Reminder set for {reminder_minutes} minutes.")
            
           
            t = Timer(reminder_time, sendReminder, [task])
            t.start()

        except ValueError:
            print("Invalid input. Reminder not set.")
    
    notification.notify(
        title="Task Added",
        message=f"'{task}' has been added to your to-do list!",
        timeout=5
    )


def sendReminder(task):
    notification.notify(
        title="Task Reminder",
        message=f"Reminder: It's time for '{task}'",
        timeout=5
    )
    print(f"Reminder: It's time for '{task}'")


def listTasks():
    if not tasks:
        print("There are no tasks in the list.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            
            print(f"{i+1}. {task}")

def deleteTask():
    listTasks()
    if tasks: 
        try:
            taskToDelete = int(input("Enter the number of the task you want to delete: "))
            if 1 <= taskToDelete <= len(tasks):
                removed_task = tasks.pop(taskToDelete - 1)
                print(f"Task '{removed_task}' deleted from the list.")
                
                notification.notify(
                    title="Task Deleted",
                    message=f"'{removed_task}' has been removed from your to-do list.",
                    timeout=5
                )
            else:
                print("Task number not valid. Please choose a number from the list.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    print("Welcome to the To Do List app with Reminders :)")
    print("---------------------------------------------------------------------------")

    while True:
        print("\nPlease select one of the following options:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()

        elif choice == "2":
            deleteTask()

        elif choice == "3":
            listTasks()

        elif choice == "4":
            print("Goodbye :)")
            break

        else:
            print("Invalid input. Please try again.")
