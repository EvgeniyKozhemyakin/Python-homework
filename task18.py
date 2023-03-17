# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# ]Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import math

length_list = int(input("Введите длину списка: "))
num = int(input("Введите число , к которому вы хотите узнать ближайшие элементы списка: "))

list = [random.randint(1,length_list) for i in range(length_list + 1)]

min_difference = int(math.fabs(list[0] - num))
min_dif_numb = list[0]

for i in range(1, length_list + 1):
    if int(math.fabs(list[i] - num)) < min_difference: 
        min_dif_numb = list[i] 
        min_difference = int(math.fabs(list[i] - num))
  
print(list)
print(min_dif_numb)