import os
os.system("cls")

def inputKeyBoard():
    while True:
        try:
            temp = input("Enter month and year separated by a space: ").split()
            if len(temp) != 2:
                print(" Please enter exactly 2 numbers month and year!")
                continue
            month, year = map(int, temp)
            if year <= 0:
                print("Year must be greater than 0")
                continue
            return month, year
        except ValueError:
            print("Invalid input! Please enter int only")
            
def calculateDay(month, year):
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        else : return 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else: return -1        

if __name__ == "__main__":
    month, year = inputKeyBoard()
    day = calculateDay(month, year)

    if(day == -1):
        print("Invalid month or year")
    else:
        print(f"{month}/{year} has {day} days")