print("Hello Ty")
amount = input("How much was your paycheck? ")
print("Your paycheck was: $",amount)
tax = float(amount) * .20
rent = float(amount) * .10
car = float(amount) * .10



print("You need to save: $"+ "{:0,.2f}".format(float(tax)) + " for taxes." )
print("You need to save: $"+ "{:0,.2f}".format(float(rent)) + " for your rent." )
print("You need to save: $"+ "{:0,.2f}".format(float(car)) + " for your car." )
netamount = float(amount) - (tax + rent + car)


print("This is how much left: $","{:0,.2f}".format(float(netamount)))