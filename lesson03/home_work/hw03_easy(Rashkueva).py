# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math


def my_round(number, ndigits):
    pass

my_round(2.1234567, 5)

# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить

print('\nЗадача 2')


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    first_number = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    second_number = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if first_number == second_number:
        return 'Счастливый билет!'
    else:
        return 'В следующий раз повезет больше'

ticket_number = input()
print(lucky_ticket(ticket_number))

