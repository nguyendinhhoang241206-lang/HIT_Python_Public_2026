import os
import math
os.system("cls")

def inputKeyBoard():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            return n
        except ValueError:
            print("Enter error value")

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = inputKeyBoard()
    if(isPrime(n)):
        print("It is a prime number")
    else:
        print("It is not prime number")