k1 = int(input("курс 1 валюты за 1 день: "))
p = int(input("% за день: "))
n = int(input("на сколько дней расчёт: "))

for i in range(0, n + 1):
    p = p * 0.01 + 1
    l = (k1 * (p + i))
    print(l)
