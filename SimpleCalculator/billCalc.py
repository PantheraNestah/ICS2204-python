def func_bill():
    amt = int(input("Enter total bill amount : "))
    tip = int(input("Choose a tip amount (10, 12 or 15)% : "))
    peopleNum = int(input("Number of people splitting bill : "))

    div_amt = float(amt / peopleNum)

    print(f"\t-> {div_amt}")
