# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


n_coins = int(input('Введите число монет на столе: '))

coins_list = []
count_eagle = count_tails = 0

for i in range(n_coins):
    coins_list.append(
        int(input(f"Монета {i + 1} лежит орлом(0) или решкой(1) вверх? Введите 0 или 1: ")))
    if coins_list[i] == 0:
        count_eagle += 1
    else:
        count_tails += 1

print(f'{coins_list} -> {count_eagle} ' if count_eagle < count_tails else f'{coins_list} -> {count_tails} ')
