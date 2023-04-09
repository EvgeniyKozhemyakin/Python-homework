# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import os


def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        print('Телефонная книга пользователя')
        for line in f:
            print(line.strip())


def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input('Введите данные контакта: '))


def find_info():
    find_info = input('Что хотите найти: ')
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def find_contact(find_info):
    contact = ''
    contact_none = 'Такого контакта нет в телефонной книге.'
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                contact = line                              
    if contact == '':print(contact_none)
    return contact


def change_file():
    name = find_contact(
        input('Введите данные контакта,которые необходимо поменять: '))
    with open("telephonebook/temp.txt", "w", encoding="UTF-8") as temp, open(path_file, 'r', encoding='UTF-8') as f:
        contact = ''
        for line in f:
            if line != name:
                temp.writelines(line)
            elif input(f'{name} Вы хотите изменить контакт ? (да/нет): ') == 'да'.casefold():
                    contact = input('Введите новые данные контакта: ')
                    temp.writelines(contact + '\n')
                    print('Контакт изменен!')
            else: 
                temp.writelines(name)    
    os.remove('telephonebook/telephonebook.txt')
    os.rename("telephonebook/temp.txt", "telephonebook/telephonebook.txt")


def delete_contact():
    name = find_contact(
        input('Введите данные контакта,которые необходимо удалить: '))
    with open("telephonebook/temp.txt", "w", encoding="UTF-8") as temp, open(path_file, 'r', encoding='UTF-8') as f:

        for line in f:
            if line != name:
                temp.writelines(line)
            elif input(f'Вы хотите удалить контакт: \n{name}(да/нет): ') == 'да'.casefold():
                print('Контакт изменен!')
                continue
            else:
                temp.writelines(name)

    os.remove('telephonebook/telephonebook.txt')
    os.rename("telephonebook/temp.txt", "telephonebook/telephonebook.txt")


def main():

    while input('Вы хотите поработать в телефонной книге (да/нет): ') == 'да'.casefold():
        print('1 - Посмотреть весь справочник \
              \n2 - Добавить новый контакт \
              \n3 - Изменить контакт в телефонной книге \
              \n4 - Удалить контакт ')

        chapter = input('Выберете цифру соответствующего раздела: ')
        if chapter == '1':
            read_file()
        elif chapter == '2':
            write_file()
        elif chapter == '3':
            change_file()
        elif chapter == '4':
            delete_contact()
        else:
            print('Такого раздела нет.')


path_file = r'telephonebook/telephonebook.txt'

if __name__ == '__main__':
    main()
