import os
os.system("cls")

def inputKeyBoard():
    while True:
        n = int(input('Enter a integer number( 20 <= n <= 30): '))
        if n >= 20 and n <= 30:
            break
    x = float(input("Enter a float number: "))
    return n, x

def calculate(n, x):
    P = 2022 * ( x ** n)
    for i in range(1, n + 1):
        P += n / (x ** n)
    return P

if __name__ == "__main__":
    n, x = inputKeyBoard()
    print(f"Result: {calculate(n, x)}")