print("welcome to the tip calculator!")
bill = float(input("what is the total bill : "))
tip = int(input("please share hw much tip you want to give 10,12 or 15?: "))
people = int(input("please share how many people are there?: "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")