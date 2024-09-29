n = int(input("введите число: "))

for i in range(0, n+1):
    if i == 0:
        pass
    elif n % i == 0 and i % 2 ==0:
        print(i)
    else:
        pass
