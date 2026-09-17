while True:
    print("\n--- Calculator Menu ---")
    print("+ : Addition")
    print("- : Substraction")
    print("* : Multiplication")
    print("/ : Division")
    print("! : Factorial")
    print("exit : Exit")
    op = input("Enter operator: ")
    if op == "exit":
        print("Calculator closed.")
        break
    elif op == "!":
        num = int(input("Enter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print(f"Result: {fact}")
    elif op in ["+","-","/","*"]:
        A = int(input("Enter first no: "))
        B = int(input("Enter second no: "))
        if op == "+":
            print(f"Result: {A + B}")
        elif op == "-":
            print(f"Result: {A - B}")
        elif op == "*":
            print(f"Result: {A * B}")
        elif op == "/":
            if B == 0:
                print("Error:Cannot divide by zero")
            else:
                print(f"Result: {A / B}")
    else:
        print("Invalid operator entered")

        
