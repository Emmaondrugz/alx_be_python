sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."

weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == "sunny":
	print(f"{sunny}")
elif weather == "rainy":
	print(f"{rainy}")
elif weather == "cold":
	print(f"{cold}")
else:
	print("Sorry, I don't have recommendations for this weather.")