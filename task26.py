# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
# 2 2
def exponentiation(num1, num2):
    if num2 < 1: 
        return 1
    return num1 * exponentiation(num1, num2 - 1)

number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

print(exponentiation(number_a, number_b))