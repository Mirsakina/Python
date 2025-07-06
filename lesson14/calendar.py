import datetime

def is_future_date(date_str):
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        return input_date >= today
    except ValueError:
        return False

calendar = {}

while True:
    print("\n--- Calendar App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Please choose an option:\n>> ")

    if choice == "1":
        date = input("Please enter the date (YYYY-MM-DD):\n>> ")
        if not is_future_date(date):
            print("Дата должна быть сегодняшней или в будущем. Попробуйте снова.")
            continue
        task = input("Please enter the task:\n>> ")
        if date in calendar:
            calendar[date].append(task)
        else:
            calendar[date] = [task]
        print("Task added!")


    elif choice == "2":
        date = input("Please enter the date to view tasks:\n>> ")
        if date in calendar:
            print(f"Tasks for {date}:")
            tasks = calendar[date]
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
        else:
            print("No tasks found for this date.")

    elif choice == "3":
        date = input("Please enter the date of the task to edit:\n>> ")
        if date in calendar:
            tasks = calendar[date]
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            task_num = input("Please enter the task number to edit:\n>> ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(calendar[date]):
                new_task = input("Please enter the new task:\n>> ")
                calendar[date][int(task_num) - 1] = new_task
                print("Task updated!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks found for this date.")

    elif choice == "4":
        date = input("Please enter the date of the task to delete:\n>> ")
        if date in calendar:
            tasks = calendar[date]
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            task_num = input("Please enter the task number to delete:\n>> ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(calendar[date]):
                removed_task = calendar[date].pop(int(task_num) - 1)
                print(f"Deleted task: {removed_task}")
                if len(calendar[date]) == 0:
                    del calendar[date] 
            else:
                print("Invalid task number.")
        else:
            print("No tasks found for this date.")
        continue
    elif choice == "5":
        exit("Terminal is closed.")
    else:
        print("Please choose from 1 to 5")
        continue  