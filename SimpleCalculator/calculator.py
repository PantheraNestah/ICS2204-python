# SCT211-0071/2022 Gift Nestah

def func_add():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1) + int(num2))

def allOperations():
    name = input("Enter your name: ")
    print("Welcome " + name)
    sum = func_add()
    print("Sum is: " + str(sum))
   

allOperations()
