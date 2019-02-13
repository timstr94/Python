"""
Homework 7.3: Calculator

Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""

number1=float(input("Select your first number:"))
number2=float(input("Select your second number:"))

while True:
    operator=input("Select your operator (+,-,*,/): ")
    if operator in ["+", "-","*", "/"]:
        break
    else:
        print("Invalid operator")

if operator=="+":
    print(float(number1+number2))
elif operator=="-":
    print(float(number1-number2))
elif operator=="*":
    print(float(number1*number2))
elif operator == "/":
    print(float(number1/number2))
else:
    print("Unavailable Operator")

