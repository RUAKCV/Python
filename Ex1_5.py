gain = float(input("Insert earned value"))
opexes = float(input ("Insert expenses"))

if gain > opexes:
    profit = gain/opexes
    print(f"Gain is greater than expenditures and profit is {profit:02}")
    number_of_emplyees = int(input ("How many employees do you have?"))
    value = gain/number_of_emplyees
    print(f"Gain per employee is {value:.2f}")

if opexes > gain:
    print("Expenditures are greater than earned value")