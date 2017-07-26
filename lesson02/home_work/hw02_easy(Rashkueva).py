# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()

print('Задача 1')
a = ['яблоко', 'банан', 'киви', 'арбуз']
for i, a in enumerate(a):
    print('{}. {}'.format(i + 1, a, '>'))
    
# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке

print('\nЗадача 2')
import random
first_list = [random.randint(-10, 10) for i in range(random.randint(10, 20))]
second_list = [random.randint(-10, 10) for i in range(random.randint(10, 20))]
print(first_list)
print(second_list)
first_list = set(first_list)
second_list = set(second_list)
p = first_list & second_list
print(p)
first_list -= p
print(first_list)

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.

print('\nЗадача 3')
rand_list = [random.randint(-10, 10) for i in range(random.randint(10, 20))]
print(rand_list)
new_rand_list = []
for w in rand_list:
    if w % 2 == 0:
        new_rand_list.append(w / 4)
    else:
        new_rand_list.append(w * 2)
print(new_rand_list)
