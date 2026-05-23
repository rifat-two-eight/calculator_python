number1 = float(input("enter number1 : "))
number2 = float(input("enter number2 : "))

print("enter an operation : ")
print("+")
print("-")
print("*")
print("/")

operation = input("Operation : ")

if operation == "+":
    print("addition :",number1+number2)

elif operation == "-":
    print("substraction :",number1-number2)

elif operation == "*":
    print("multiplication :",number1*number2)

elif operation == "/":
    if number1  == 0:
        print("this output always zero")
    elif number2 == 0:
        print("not divisible")
    else:
        print("division :",number1/number2)

else:
    print("not a valid number")