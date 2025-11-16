task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
is_time_bound = input("Is it time-bound? (yes/no): ")

match priority:
	case "high":
		if is_time_bound:
			print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
		else:
			print(f"Note: {task} is a high priority task. Consider completing it when you are free.!")
	case "medium":
		if is_time_bound:
			print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
		else:
			print(f"Note: {task} is a medium priority task. Consider completing it when you are free.!")
	case "low":
		if is_time_bound:
			print(f"Reminder: {task} is a Low priority task that requires immediate attention today!")
		else:
			print(f"Note: {task} is a Low priority task. Consider completing it when you are free.!")