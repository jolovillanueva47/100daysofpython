print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill? $"))
percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))*.01
split=int(input("How many people to split the bill? "))
calculation=round((((total_bill*percentage)+total_bill)/split),2)
print(f"Each person should pay: ${calculation}")