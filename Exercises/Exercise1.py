# Genrate a calculator which will solve the problem correctly except for given calculations :
# a) 35*5 =555, b) 22+4=28, c) 41-23 = 11
operator = input("Enter operatin to be performed: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
if num1 == 35 and num2 == 5 and operator== "*":
    print(555)
elif num1 == 22 and num2 == 4 and operator== "+":
    print(28)
elif num1 == 41 and num2 == 23 and operator== "-":
    print(111)
else:
    if operator=="+":
        print(num1 + num2)
    elif operator=="-":
        print(num1 - num2)
    elif operator=="*":
        print(num1 * num2)
    elif operator=="/":
        print(num1 / num2)
    else:
        print("Provide valid input")
