prices = {
    'rice': 50,
    'wheat': 40,
    'sugar': 30,
    'oil': 120
}
quantities = {
    'rice': 2,     
    'wheat': 1,    
    'sugar': 3,    
    'oil': 1       
}
total_bill = 0

for item in prices:
    if item in quantities:
        item_total = prices[item] * quantities[item]
        total_bill += item_total
        print(f"{item}: {quantities[item]} x {prices[item]} = {item_total}")

print("\nTotal Bill:", total_bill)
