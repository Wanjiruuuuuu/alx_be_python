
# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        note = f"'{task}' is a low priority task."
    case _:
        note = "Invalid priority level entered."

# Add time sensitivity if applicable 
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    note += " Consider completing it when you have free time."
else:
    note += " Time sensitivity was not specified correctly."

# Print the customized reminder
print("\nReminder:", reminder)


