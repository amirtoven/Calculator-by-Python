#Program by tel:@amirrezatavanaee

print("Welcome to Calculator")
print("Select a Calculation Operation: \n + \n - \n / \n *")
uinput = input("Select: ")

def Plus():
    value1 = int(input("Enter first value: "))
    value2 = int(input("Enter second value: "))
    result = value1 + value2
    print(f"the result of {value1} + {value2} is {result}")

def Minus():
    value1 = int(input("Enter first value: "))
    value2 = int(input("Enter second value: "))
    result = value1 - value2
    print(f"the result of {value1} - {value2} is {result}")

def Devide():
    value1 = int(input("Enter first value: "))
    value2 = int(input("Enter second value: "))
    result = value1 / value2
    print(f"the result of {value1} / {value2} is {result}")

def Cross():
    value1 = int(input("Enter first value: "))
    value2 = int(input("Enter second value: "))
    result = value1 * value2
    print(f"the result of {value1} * {value2} is {result}")

if uinput == "1" or uinput == "Plus" or uinput == "+":
    print("The operation is Plus")
    Plus()
elif uinput == "2" or uinput == "Minus" or uinput == "-":
    print("The operation is Minus")
    Minus()
elif uinput == "3" or uinput == "Devide" or uinput == "/":
    print("The operation is Devide")
    Devide()
elif uinput == "4" or uinput == "Cross" or uinput == "*":
    print("The operation is Cross")
    Cross()
else:
    print("Error")