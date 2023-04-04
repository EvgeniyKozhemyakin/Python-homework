# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
       for line in f:
          print(line.strip())

def write_file():
    with open(path_file,'a',encoding='UTF-8' ) as f:
        f.writelines('\n' + input())

def find_info():
    find_info = input('Что хотите найти: ')
    with open(path_file,'r',encoding='UTF-8' ) as f:       
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)

def change_file():
    find_info = input()
    new_info = input()
    with open(path_file,'r+',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue

        
def main():
    print(path_file)
    change_file()

path_file = r'telephonebook/telephonebook.txt'

if __name__ == '__main__':
    main()