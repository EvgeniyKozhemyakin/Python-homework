# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def checking_set_for_repetitions (set_number):
    set_of_number_not_repetitions = []
    for i in set_number:
        if i not in set_of_number_not_repetitions:
            set_of_number_not_repetitions.append(i)
    return set_of_number_not_repetitions   

n_set_of_numbers = int(input('Введите длину первого множества : '))
first_set_numbers = [int(input('Введите целые числа первого множества: ')) for i in range(0, n_set_of_numbers)]
m_set_of_numbers = int(input('Введите длину второго множества : '))
second_set_numbers = [int(input('Введите целые числа второго множества: ')) for i in range(0, m_set_of_numbers)]
    
not_repeat_set_m_and_n =  sorted(checking_set_for_repetitions(first_set_numbers + second_set_numbers))

print(*not_repeat_set_m_and_n)
