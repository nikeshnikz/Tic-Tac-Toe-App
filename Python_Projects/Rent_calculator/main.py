rent = float(input("Enter your hostel/Flat rent = "))
food = float(input("Enter the Amount of food ordered = "))
electricity_spend = float(input("Enter the total  electricity  spend = "))
charge_per_unit = float(input("Enter the charge per unit = "))
persons = float(input("Enter the number of persons living  in flat/room = "))


total_elctricity_bill = electricity_spend * charge_per_unit

output = (food + rent + total_elctricity_bill) // persons

print(f"Each person will  pay  : {output} RS")

