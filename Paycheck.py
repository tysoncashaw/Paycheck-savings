print("Hello Ty")
amount = input("How much was your paycheck? ")
print("Your paycheck was: $",amount)
tax = float(amount) * .20
print("You need to save: $"+ "{:0,.2f}".format(float(tax)) + " for taxes." )