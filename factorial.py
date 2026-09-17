def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(int(input("enter a number ; "))))  #

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     elif n < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         return n * factorial(n - 1)
# num = int(input("enter a number : "))
# print(f"The factorial of {num} is {factorial(num)}")