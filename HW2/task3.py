import os
import math
os.system("cls")

def inputKeyBoard():
    while True:
        try:
            temp = int(input("Enter a positive integer number: "))
            return temp
        except ValueError:
            print("Invalid input!")

def testSum(temp):
    x = str(temp)
    count = 0
    sum = 0
    for i in x:
        count += 1
        sum += int(i)
    return count, sum

def testPrime(temp):
    if temp < 2:
        return False
    if temp == 2:
        return True
    for i in range(2, math.isqrt(temp) + 1):
        if temp % i == 0:
            return False
    return True

if __name__ == "__main__":
    temp = inputKeyBoard()
    count, sum = testSum(temp)
    if testPrime(temp):
        print(f"Digit count: {count}, Digit sum: {sum}, {temp} was a prime number.")
    else: 
        print(f"Digit count: {count}, Digit sum: {sum}, {temp} was not a prime number.")