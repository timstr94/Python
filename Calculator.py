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
operator=input("Choose your Operator (+,-,*,/):")

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

