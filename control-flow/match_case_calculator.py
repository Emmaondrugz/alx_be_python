first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
	case "+":
		result = first_num + second_num
		print(f"The result is {result}")
	case "-":
		result = first_num - second_num
		print(f"The result is {result}")
	case "*":
		result = first_num * second_num
		print(f"The result is {result}")
	case "/":
		if second_num == 0:
			print("Cannot divide by zero")
		else:
			result = first_num / second_num
			print(f"The result was {result}")

