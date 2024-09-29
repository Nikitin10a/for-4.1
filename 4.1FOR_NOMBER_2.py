a = int(input("начальный член: "))
r = int(input("знаменатель: "))
n = int(input("количество членов: "))

for b in range(0, n):
    b = (a * (r ** (n - 1)))
    print(b)