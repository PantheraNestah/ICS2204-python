# SCT211-0071/2022 Gift Nestah
def func_bill():
    amt = int(input("Enter total bill amount : "))
    tip = int(input("Choose a tip amount (10, 12 or 15)% : "))
    peopleNum = int(input("Number of people splitting bill : "))
    amt += amt * (tip * 0.01)

    div_amt = float(amt / peopleNum)

    print(f"\n\t-> {div_amt:.2f}")

func_bill()
