# without try except

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
add = int(num1) + int(num2)
subtract = int(num1) - int(num2)
mul = int(num1) * int(num2)
div = int(num1) / int(num2)
avg = (int(num1) + int(num2))/2.0
print(f"Sum of 2 numbers is {add}")
print(f"Subtraction of 2 numbers  is {subtract}")
print(f"Multiplication  of 2 numbers  is {mul}")
print(f"Division of 2 numbers  is {div}")
print(f"Average of 2 numbers  is {avg}")

# with try except
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    add = int(num1) + int(num2)
    subtract = int(num1) - int(num2)
    mul = int(num1) * int(num2)
    div = int(num1) / int(num2)
    avg = (int(num1) + int(num2))/2.0
    print(f"Sum of 2 numbers is {add}")
    print(f"Subtraction of 2 numbers  is {subtract}")
    print(f"Multiplication  of 2 numbers  is {mul}")
    print(f"Division of 2 numbers  is {div}")
    print(f"Average of 2 numbers  is {avg}")
except ValueError:
    print("Could not convert data to an integer.")
