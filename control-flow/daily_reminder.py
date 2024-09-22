def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder = ""

    # Process the task based on priority using Match Case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        print(f"{reminder} that requires immediate attention today!")
    else:
        print(f"{reminder}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()