task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = print("{task} is a high priority task.")
    case "medium":
        reminder = print("{task} is a medium priority task.")
    case "low":
        reminder = print("{task} is a low priority task.")
    case _:
        reminder = print("Invalid priority level entered.")

if time_bound == "yes":
    reminder = "It requires immediate attention today!"
elif time_bound == "no":
    reminder = "Consider completing it when you have free time."
else:
    reminder = "Invalid time sensitivity input."        
print("Reminder: {reminder}")
