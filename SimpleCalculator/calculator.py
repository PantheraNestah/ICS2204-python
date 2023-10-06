# SCT211-0071/2022 Gift Nestah

def func_add():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1) + int(num2))

def func_ageCalc():
    year = int(input("Enter your year of birth: "))
    age_years = 2023 - year
    age_months = age_years * 12
    age_days = age_months * 30

    print(f"You are {age_years} years old")
    print(f"You are {age_months} months old")
    print(f"You are approximately {age_days} days old")

def allOperations():
    name = input("Enter your name: ")
    print("Welcome " + name)
    sum = func_add()
    print("Sum is: " + str(sum))
    func_ageCalc()
    
   

allOperations()
