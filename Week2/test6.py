import os
os.system("cls")

def inputKeyBoard():
    while True:
        n = int(input('Enter a integer number( 100 <= n <= 200): '))
        if n >= 100 and n <= 200:
            return n

def calculate(n, x):
    P = 2022 * ( x ** n)
    for i in range(1, n + 1):
        P += n / (x ** n)
    return P

if __name__ == "__main__":
    n, x = inputKeyBoard()
    print(f"Result: {calculate(n, x)}")