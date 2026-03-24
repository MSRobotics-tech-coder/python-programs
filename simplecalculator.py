# python program to make a simple calculator

# difining two numbers for calculation
num1 = float(input("-->"))
num2 = float(input("-->"))

# function to add two numbers
def add(num1 , num2):
    return num1 + num2

# function to substract two numbers
def subtract(num1 , num2):
    return num1 - num2

# function to multiply two numbers
def multiply(num1 , num2):
    return num1 * num2

# function to divide two numbers
def divide(num1 , num2):
    return num1 / num2


print("Choose from the following operations "
          "+ , - , * , /")

operation = input("Enter operation :- ")

# applying condition
if (operation == "+"):
    print(num1 + num2)

elif (operation == "-"):
    print(num1 - num2)

elif (operation == "*"):
    print(num1 * num2)

elif (operation == "/"):
    if (num2 == 0):
        print("CANNOT BE DIVIDED BY ZERO !!!!")
    else:
        print(num1 / num2)

else :
    print("Wrong input")
