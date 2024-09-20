# daily_reminder.py

# Step 1: Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match case based on priority
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task."
    case 'medium':
        reminder = f"'{task}' is a medium priority task."
    case 'low':
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."

# Step 3: Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " It requires immediate attention today!"
elif time_bound == 'no':
    reminder += " Consider completing it when you have free time."
else:
    reminder += " Invalid time-bound input. Please enter 'yes' or 'no'."

# Step 4: Print the final reminder
print(reminder)
