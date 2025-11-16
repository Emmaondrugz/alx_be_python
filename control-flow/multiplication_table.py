number = int(input("Enter a number to see its multiplication table: "))
times = 0

for x in range(1, 11):
	times += 1
	product = number * times
	print(f"{number} X {times} = {product}")