import os
os.system("cls")

def inputKeyBoard():
    a, b = input("Enter two numbers separated by a space: ").split()
    return int(a), int(b)

if __name__ == "__main__":
    print("Hello World")
    a, b = inputKeyBoard()
    print(f"The sum of two numbers are: {a} + {b} = {a + b}")
    print(f"The difference of two numbers are: {a} - {b} = {a -b}")
    print(f"The product of two numbers are: {a} * {b} = {a * b}")
    print(f"The quotient of two numbers are: {a} / {b} = {a / b: .3f}")