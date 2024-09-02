# -*- coding: cp1251 -*-

MassChar = input("Введите последовательность чисел через пробел: ").strip().split(" ")
MassNums = sorted([int(item) for item in MassChar])
del MassNums[0]
del MassNums[len(MassNums) - 1]
total = 0
for x in MassNums:
    if x < 0:
        total += x       
print(total)