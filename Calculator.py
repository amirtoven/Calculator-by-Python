# Program by tel:@amirrezatavanaee

def Plus():
    result = 0
    while True:
        userinput = input("Enter the value (or type 'done' to finish): ")
        if userinput.lower() == 'done':
            break
        try:
            number = int(userinput)
            result += number
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"The sum is: {result}")

def Minus():
    result = 0
    while True:
        userinput = input("Enter the value (or type 'done' to finish): ")
        if userinput.lower() == 'done':
            break
        try:
            number = int(userinput)
            result -= number
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"The difference is: {result}")

def Divide():
    result = None
    while True:
        userinput = input("Enter the value (or type 'done' to finish): ")
        if userinput.lower() == 'done':
            break
        try:
            number = int(userinput)
            if result is None:
                result = number
            else:
                result /= number
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"The quotient is: {result}")

def Multiply():
    result = 1
    while True:
        userinput = input("Enter the value (or type 'done' to finish): ")
        if userinput.lower() == 'done':
            break
        try:
            number = int(userinput)
            result *= number
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"The product is: {result}")

def main():
    print("Welcome to Calculator")
    print("Select a Calculation Operation:\n1. + (Plus)\n2. - (Minus)\n3. / (Divide)\n4. * (Multiply)")
    uinput = input("Select: ")

    if uinput in ["1", "+", "Plus"]:
        print("The operation is Plus")
        Plus()
    elif uinput in ["2", "-", "Minus"]:
        print("The operation is Minus")
        Minus()
    elif uinput in ["3", "/", "Divide"]:
        print("The operation is Divide")
        Divide()
    elif uinput in ["4", "*", "Multiply"]:
        print("The operation is Multiply")
        Multiply()
    else:
        print("Error: Invalid operation selected")

if __name__ == "__main__":
    main()
