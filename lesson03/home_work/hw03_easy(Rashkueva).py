# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math


print('Задача 1')


def my_round(number, ndigits):
    number = str(number)
    n, afterdot = number.split('.')
    """Здесь мы проверяем, нужно ли вообще округлять введенное число"""
    if len(afterdot) <= ndigits:
        return number
    else:
        """'Собираем' число без точки для дальнейшей арифметики"""
        slice = list(n + afterdot[:ndigits])
        """Здесь мы проверяем, пойдет ли округление вверх или вниз"""
        if int(afterdot[(ndigits - 1)]) >= 5:
            slice = list(int(slice) + 1)
        """Возвращаем число, вставляя точку на нужную позицию.
        Позицию находим, исходя из требуемого количества символов послее нее"""
        return float(''.join(slice.insert((len(slice) - ndigits), '.')))

number = float(input())
ndigits = int(input())
print(my_round(number, ndigits))

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
    return first_number == second_number

ticket_number = input()
if lucky_ticket(ticket_number):
    print('Счастливый билет!')
else:
    print('В следующий раз повезет')
