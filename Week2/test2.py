import os
import math
os.system("cls")

def inputKeyBoard():    
    a, b = input("Enter coordinates separated by a space: ").split()
    return float(a), float(b)

def euclidean(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
if __name__ == "__main__":
    print("Enter A: ")
    a = inputKeyBoard()
    print("Enter B: ")
    b = inputKeyBoard()
    print(f"The euclidean distance between two points is: {euclidean(a, b): .3f}")