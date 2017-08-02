# Все задачи текущего блока решите с помощью генераторов!

# Задание-1:
# Дан список, заполненный произвольными целыми цифрами, получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


numbers = [random.randint(-10, 10) for i in range(random.randint(5, 10))]
new_numbers = [i**2 for i in numbers]
print(numbers)
print(new_numbers)

# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

print('_____________')

fruit_list1 = ['яблоко', 'мандарин', 'груша', 'дыня', 'авокадо', 'банан']
fruit_list2 = ['апельсин', 'дыня', 'лимон', 'авокадо', 'ананас', 'яблоко']
common_fruit_list = [fruit for fruit in fruit_list1 if fruit in fruit_list2 ]
print(common_fruit_list)

# Задание-3:
# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('_____________')

rand_list = [random.randint(-20, 30) for i in range(random.randint(15, 30))]
new_rand_list = [w for w in rand_list if w % 3 == 0 and w >= 0 and w % 4 != 0]
print(rand_list)
print(new_rand_list)
