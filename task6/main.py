# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

numberTicket = int(input('Введите номер билета: '))
sumFirsThree = 0
sumLastThree = 0

if numberTicket > 999999 or numberTicket < 111110:
    while numberTicket > 999999 or numberTicket < 111110:
        print('Вы ввели неверный номер билет,пожалуйста повторите ввод')
        numberTicket = int(input('Введите номер билета из 6 цифр: '))
else :
    while numberTicket > 0:
        if numberTicket > 999:
            sumLastThree += numberTicket % 10
        else : sumFirsThree += numberTicket % 10
    numberTicket //= 10

print(f'{numberTicket} -> yes'if sumFirsThree == sumLastThree else f'{numberTicket} -> no')    
