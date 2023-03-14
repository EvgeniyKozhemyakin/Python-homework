# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого
# Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


sum_numbers = int(input('Введите сумму загаданных чисел: '))
product_numbers = int(input('Введите произведение загаданных чисел: '))

num1 = 0
num2 = 0

for i in range(sum_numbers):
    for j in range(product_numbers):
        if i * j == product_numbers and i + j == sum_numbers:
            num1, num2 = i, j
            break
print('Невозможно найти загаданные числа' if num1 == num2 == 0 else f'{sum_numbers} {product_numbers} -> {num1} {num2}')
