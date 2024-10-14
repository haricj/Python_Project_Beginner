# This function add two water
def add(x,y):
    return x+y

# This function subtracts two number
def subtract(x,y):
    return x-y

# This function multiples two number
def multiply(x,y):
    return x*y

# This function devides two number
def divide(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from user
    choice=input("Enter choice 1/2/3/4 ")

    # check if the choice is one of the digit listed
    if choice.isdigit():
        if 1<=int(choice)<=4 :
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else: 
            print("Invalid Input, Please input the number gain")
    else:
        print("Invalid Input, Please input the number gain")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    next_calculation=input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")
