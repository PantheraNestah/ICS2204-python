def func_bill():
    amt = int(input("Enter total bill amount : "))
    tip = int(input("Choose a tip amount (10, 12 or 15)% : "))
    peopleNum = int(input("Number of people splitting bill : "))

    div_amt = float(amt / peopleNum)

    print(f"\n\t-> {div_amt:.2f}")

func_bill()
