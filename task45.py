# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары
# дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284

import datetime

a = datetime.datetime.now()

def sum_divide(number):
    sum_divide, i = 1, 2

    while i*i < number:
        if number % i == 0:
            sum_divide += i
            sum_divide += (number//i)
        i += 1

    return sum_divide

k, i = 100000, 1
while i < k:
    j = sum_divide(i)
    if i < j < k and i == sum_divide(j):
        print(f'{i} {j}')
    i += 1

print(datetime.datetime.now() - a)
