task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print("{task} is a high priority task.")
    case "medium":
        print("{task} is a medium priority task.")
    case "low":
        print("{task} is a low priority task.")
    case _:
        print("Invalid priority level entered.")

if time_bound == "yes":
    print("It requires immediate attention today!")
elif time_bound == "no":
    print("Consider completing it when you have free time.")
else:
    print("Invalid time sensitivity input.")        