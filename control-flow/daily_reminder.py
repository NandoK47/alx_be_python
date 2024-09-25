task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

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
    reminder += print("It requires immediate attention today!")
elif time_bound == "no":
    reminder += print("Consider completing it when you have free time.")
else:
    reminder += print("Invalid time sensitivity input.")        