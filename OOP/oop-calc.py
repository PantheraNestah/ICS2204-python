# SCT211-0071/2022 Gift Nestah

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def func_add(self):
        sum = self.num1 + self.num2
        print (f"The sum of {self.num1} and {self.num2} is: {sum}")

    def func_diff(self):
        sum = self.num1 - self.num2
        print (f"The difference between {self.num1} and {self.num2} is: {sum}")

    def func_mult(self):
        sum = self.num1 * self.num2
        print (f"The product of {self.num1} and {self.num2} is: {sum}")

    def func_div(self):
        try:
            sum = self.num1 / self.num2
            print (f"The division of {self.num1} by {self.num2} is: {sum}")
        except:
            raise ZeroDivisionError("Division by zero is undefined!")
        finally:
            print("For valid division operations, num2 should be greater than 0")

    def func_modul(self):
        sum = self.num1 % self.num2
        print (f"The modulus between {self.num1} and {self.num2} is: {sum}")

    def func_ageCalc(self):
        year = int(input("Enter your year of birth: "))
        age_years = 2023 - year
        age_months = age_years * 12
        age_days = age_months * 30

        print(f"You are {age_years} years old")
        print(f"You are {age_months} months old")
        print(f"You are approximately {age_days} days old")
calc1 = Calculator(13, 43)
calc1.func_add()
calc1.func_diff()
calc1.func_div()
calc1.func_mult()
calc1.func_modul()

calc1.func_ageCalc()
calc3 = Calculator(13,0)
calc3.func_div()
