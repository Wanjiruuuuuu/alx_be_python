

# daily_reminder.py

# Prompt for task details
task = input("Enter yor task for today: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires your immediate attention!")

        else : 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires your immediate attention!")

        else: 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time. ")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires your immediate attention!")

        else : 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        





        
