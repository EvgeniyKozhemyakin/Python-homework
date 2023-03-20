# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

length_list = int(input("Введите длину списка: "))
num_from_list = int(input(f"Введите число(от 1 до {length_list}) , повторения которого вы хотите узнать: "))

count_num = 0
list = [random.randint(1,length_list) for i in range(length_list + 1)]

for i in range(len(list)):
    if num_from_list == list [i]:
        count_num += 1 

print (f'{list} -> {count_num} ')




