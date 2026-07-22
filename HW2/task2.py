import os
os.system("cls")

def inputKeyBoard():
    while True:
        try:
            temp = input("Enter day and month separated by a space: ").split()
            if len(temp) != 2:
                print("Please enter exactly 2 numbers day and month")
                continue
            day, month = map(int, temp)
            if testDay(day, month) == False:
                print("Invalid day, month")
                continue
            return day, month
        except ValueError:
            print("Invalid input! Please enter int only")

def testDay(day, month):
    if day > 0:
        if month == 2 and day < 30:
            return True
        elif month in [4, 6, 9, 11] and day < 31:
                return True
        elif month in [1, 3, 5, 7, 8, 10, 12] and day < 32:
            return True
    return False

def findZodiac(day, month):
    if (month == 3 and day > 20) or (month == 4 and day < 20):
        return "Bach Duong"
    elif (month == 4 and day > 19) or (month == 5 and day < 21):
        return "Kim Nguu"
    elif (month == 5 and day > 20) or (month == 6 and day < 21):
        return "Song Tu"
    elif (month == 6 and day > 20) or (month == 7 and day < 23):
            return "Cu Giai"
    elif (month == 7 and day > 22) or (month == 8 and day < 23):
            return "Su Tu"
    elif (month == 8 and day > 22) or (month == 9 and day < 23):
            return "Xu Nu"
    elif (month == 9 and day > 22) or (month == 10 and day < 23):
            return "Thien Binh"
    elif (month == 10 and day > 22) or (month == 11 and day < 22):
            return "Bo Cap"
    elif (month == 11 and day > 21) or (month == 12 and day < 22):
            return "Nhan Ma"
    elif (month == 12 and day > 21) or (month == 1 and day < 20):
            return "Ma Ket"
    elif (month == 1 and day > 19) or (month == 2 and day < 19):
            return "Bao Binh"
    else:
        return "Song Ngu"

if __name__ == "__main__":
    day, month = inputKeyBoard()
    print(f" {day}/{month} was {findZodiac(day, month)}")