pattern = int(input("Enter the size of the pattern: "))
num = 1

while num <= pattern:
	for x in range(1, pattern + 1):
		print("*", end="")
	print()
	num += 1
	
	