# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчеты заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП
# пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

# С использованием классов.
# Рализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла

with open('data/workers.txt', 'w+', encoding='UTF-8') as f:
    f.write('Иванов 240 168\nПетров 200 168\nСидоров 250 168\nПупкин 220 168\nКазакова 230 168')

with open('data/workers.txt', 'r', encoding='UTF-8') as f:
    worker_list = f.read()
    print(type(worker_list))

with open('data/hours_of.txt', 'w+', encoding='utf-8') as h:
    h.write('Иванов 168\nПетров 140\nСидоров 180\nПупкин 166\nКазакова 170')

with open('data/hours_of.txt', 'r', encoding='utf-8') as h:
    hours_list = h.read()
    print(hours_list)

worker_date = worker_list.split('\n')
print(worker_date)

class Worker:

    def __init__(self, date):
        self.date = worker_list[i]


