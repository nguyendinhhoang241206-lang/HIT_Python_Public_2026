import os
import math
os.system("cls")

def inputKeyBoard():
    return float(input("Enter a float number: "))

def solveQuadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("The equation has no solution!")
    elif delta == 0: 
        print(f"The equation has a double root x1 = x2 = {-b / ( 2 * a)}")
    else:
        print(f"The equation has two different solutions x1 = {(-b + math.sqrt(delta)) / (2 * a)} and x2 = {(-b - math.sqrt(delta)) / (2 * a)}")

if __name__ == "__main__":
    print("Enter a, b, c of equation ax^2 + bx + c: ")
    a = inputKeyBoard()
    b = inputKeyBoard()
    c = inputKeyBoard()
    solveQuadratic(a, b, c)