# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1

print('Задача 1')


def fibonacci(n, m):
    line = []
    a, b = 1, 1
    for i in range(m-2):
        a, b = b, a + b
        if i >= n - 3:
            line.append(b)
    return line

n = int(input())
m = int(input())
print(fibonacci(n, m))

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()

print('\nЗадача 2')


def sort_to_max(origin_list):
    sorted_list = []
    for n in origin_list:
        inserted = False
        for i in range(len(sorted_list)):
            if n < sorted_list[i]:
                sorted_list.insert(i, n)
                inserted = True
                break
        if not inserted:
            sorted_list.append(n)
    return sorted_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

