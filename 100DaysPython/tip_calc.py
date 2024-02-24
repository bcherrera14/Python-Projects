print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip_percent = float(input("How much would you like to tip? "))
split_num = float(input("How many people to split the bill? "))
total_with_tip = total + total*(tip_percent/100)
split_price = '{:.2f}'.format(round(total_with_tip / split_num, 3))

print(f"Each person should pay ${split_price}")