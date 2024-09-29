a = int(input("цена: "))
b = int(input("скидка: "))

a1 = 0
for i in range(1, 10):
    a1 = (a - (b * 0.01 * a * i))
    print("цена за 10 товар")
    print(a1)