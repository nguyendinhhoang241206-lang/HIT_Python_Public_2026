a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a < b:
    print("a < b")
elif a == b:
    print("a = b")
else:
    print("a < b")

a = [1, 2, 3 , 5]
sum = 0
for i in range(1, 4):
    sum += a[i]
print(sum)
