n = int(input("сколько лет: "))
p = int(input("начальная численность: "))
r = int(input("процентный прирост: "))

for i in range(0, n+1):
    P = (r * i)
    l = p + P
    print(l)