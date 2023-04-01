import tkinter as tk


def calc():
    operator = input("Enter operator (+, -, *, /):")
    num1 = float(input("Enter first number."))
    num2 = float(input("Enter second number"))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Operator not found!")
    print("The result is: " + str(result))

app = True
while app == True:
    calc()
    exit = input("If u want to continue press w. /n If u want to exit press x: ")
    if exit == "x":
        exit()