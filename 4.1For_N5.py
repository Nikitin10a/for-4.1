n = int(input("количество чисел: "))

s1 = 0
s2 = 0
s3 = 0
for i in range(0, n+1):
    s1 += i
    print("сумма")
    print(s1)
    s2 *= i
    print("произведение")
    print(s2)
    s3 = (i + i + 1) / n
    print("среднее")
    print(s3)


