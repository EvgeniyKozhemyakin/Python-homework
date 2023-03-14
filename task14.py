# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10
n = int(input("Введите число: "))

power_numbers = []
i = 0

while 2 ** i < n:
    power_numbers.append(2**i)
    i += 1

print(f'{n} -> {power_numbers}')
