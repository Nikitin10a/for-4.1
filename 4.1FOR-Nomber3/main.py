n = int(input("количество чисел: "))
s1 = 0
s2 = 0
for i in range(0, n):
    if i % 2 == 0:
        s1 += 1
    else:
        s2 += 1

print("чётных")
print(s1)
print("нечётных")
print(s2)
