food_prices = [("Burger", 50), ("Pizza", 100), ("Fries", 30)]
sorted_food_prices = sorted(food_prices, key=lambda x: x[1], reverse=True)
print("Sorted food prices:", sorted_food_prices)
