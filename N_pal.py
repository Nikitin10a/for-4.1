n = int(input("Введите число n(до 100000): "))
for i in range(100, n):
    if 100 < i < 1000:
        if (i // 100) == (i % 10):
            print(i)
    elif 1000 < i < 10000:
        if (i // 1000) == (i % 10) and ((i // 100) % 10) == ((i % 100) // 10):
            print(i)
    elif 10000 < i < 100000:
        if (i // 10000) == (i % 10) and ((i // 1000) % 10) == ((i % 100) // 10):
            print(i)
    
