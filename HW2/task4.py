import os
os.system("cls")

def inputKeyBoard():
    while True:
        try:
            temp = int(input("Enter money (positive integer): "))
            if temp <= 0:
                print("Money must be greater than 0!")
                continue
            return temp
        except ValueError:
            print("Invalid input!") 

def findSum(temp):
    count = temp // 28
    x = count
    while x > 2:
        new = x // 3
        old = x % 3
        count += new 
        x = new + old
    return count
    

if __name__ == "__main__":
    temp = inputKeyBoard()
    print(f"Number of beer bottles that can be bought: {findSum(temp)}")