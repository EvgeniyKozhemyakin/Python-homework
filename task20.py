# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# , G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
#     12


dict_enru1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N',
                           'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
dict_enru2 = dict.fromkeys(['G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2)
dict_enru3 = dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
dict_enru4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 4)
dict_enru5 = dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
dict_enru8 = dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8)
dict_enru10 = dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10)
dict_scrabble = dict_enru1 | dict_enru2 | dict_enru3 | dict_enru4 | dict_enru5 | dict_enru8 | dict_enru10


word_user = (input('Введите слово: ')).upper()
count_score = 0
flag = True

while (flag):
    for letters in word_user:
        if letters not in dict_scrabble:
            word_user = (
                input('Ошибка при вводе! Таких символов нет в игре. Введите слово: ')).upper()
            break
        else:
            flag = False
            count_score += dict_scrabble[f'{letters}']

print(count_score)
