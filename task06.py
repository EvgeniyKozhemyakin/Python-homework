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

while numberTicket > 999999 or numberTicket < 100000:
    print('Вы ввели неверный номер билет,пожалуйста повторите ввод')
    numberTicket = int(input('Введите номер билета из 6 цифр: '))

temp = numberTicket
while temp > 0:
    if temp > 999:
        sumLastThree += temp % 10
    else:
        sumFirsThree += temp % 10
    temp //= 10

print(f'{numberTicket} -> yes'if sumFirsThree ==
      sumLastThree else f'{numberTicket} -> no')
