class Calculator:
    def __init(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def func_add():
        sum = self.num1 + self.num2
        print (f"The sum of {self.num1} and {self.num2} is: {sum}")

    def func_ageCalc():
        year = int(input("Enter your year of birth: "))
        age_years = 2023 - year
        age_months = age_years * 12
        age_days = age_months * 30

        print(f"You are {age_years} years old")
        print(f"You are {age_months} months old")
        print(f"You are approximately {age_days} days old")