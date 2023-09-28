# SCT211-0071/2022 Gift Nestah

def func_add():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1) + int(num2))

def func_subtract():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1) - int(num2))

def func_multiply():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1) * int(num2))

def func_divide():
    num1 = input("First number: ")
    num2 = input("Second number: ")

    return (int(num1 )/ int(num2))

def allOperations():
    condition = True
    while (condition):
        print("\nChoose Operation to carry out")
        print(
            """
                \n\t1.Addition
                \n\t2.Subtraction
                \n\t3.Multiplication
                \n\t4.Division
                \n\t5.Exit
            """
        )
        choice = input("\nEnter choice...")
        if (choice == "5"):
            condition = False
        elif (choice == "1"):
            print(f"Sum is: {func_add()}")
        elif (choice == "2"):
            print(f"Difference is: {func_subtract()}")
        elif (choice == "3"):
            print(f"Product is: {func_multiply()}")
        else:
            print(f"Division equals: {func_divide()}")

allOperations()
