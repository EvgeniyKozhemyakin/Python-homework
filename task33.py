# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def change_max_min(list_num):
#     min_value = min(list_num)
#     max_value = max(list_num)
#     for i in range(len(list_num)):
#         if list_num[i] == max_value:
#           list_num[i] = min_value
#     return list_num            

# n = int(input('введите число оценок: '))
# estimates = [int(input('введите оценку: ')) for i in range(n)]

# print(estimates)
# print(change_max_min(estimates))

def min_max_search(input_list):
    return min(input_list), max(input_list)


def min_max_replace(start_list: list[int], copy: bool =True) -> list[int]:  ## Type Hinting
    if copy:
        start_list = start_list.copy()
    min_el, max_el = min_max_search(start_list)
    while max_el in start_list:
        max_index = start_list.index(max_el)
        start_list[max_index] = min_el
    return start_list



start_list = [1, 4, 3, 5, 4]
print(min_max_replace(start_list))
