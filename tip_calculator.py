print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? rs "))
tip = int(input("How much tip would you like to give? 50 , 100 , 150 , 200 "))
people = int(input("How many people to split the bill? "))
total_bill = bill + tip
print(f"Total Bill = {total_bill}")
bill_for_each = total_bill/people
print(f"Everyone will give { bill_for_each } rupees each")