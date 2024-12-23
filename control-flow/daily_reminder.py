

# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task and provide a single output
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"\nNote: '{task}' is a high priority task that can be completed when you have free time.")
        else:
            print(f"\nReminder: '{task}' is a high priority task with an unspecified time sensitivity.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"\nNote: '{task}' is a medium priority task that can be completed when you have free time.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task with an unspecified time sensitivity.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"\nNote: '{task}' is a low priority task that can be completed when you have free time.")
        else:
            print(f"\nReminder: '{task}' is a low priority task with an unspecified time sensitivity.")
    case _:
        print("\nInvalid priority level entered.")
