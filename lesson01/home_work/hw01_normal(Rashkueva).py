# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
import random
n = random.randint(0, 1000000)
print(n)
n = str(n)
L = list(n)
print(max(L))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
print('Введите переменную a')
print('Введите переменную b')
a = int(input())
b = int(input())
a,b = b,a
print('a=' + str(a) + ', b=' + str(b) + '.')

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
print('Введите значения переменных a, b и c:')
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if d > 0:
    first = ((-b + math.sqrt(d))/(2 * a))
    second =((-b - math.sqrt(d))/(2 * a))
    print('x1 = %.2f, x2 = %.2f' % (first, second))
elif d == 0:
    single = -b / (2 * a)
    print('x = %.2f' % single)
else:
    print('Корней нет')
