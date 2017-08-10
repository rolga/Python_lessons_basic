# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:

    def __init__(self, classes):
        self.classes = classes

    def classlist(self):
        for classroom in classes:
            print(classroom.title)

class Person:

    def __init__(self, name):
        self.name = name


class Classroom:

    def __init__(self, title, teachers):
        self.title = title
        self.teachers = teachers


class Subject:

    def __init__(self, title):
        self.title = title


class Student(Person):

    def __init__(self, name, classroom, mom, dad):
        Person.__init__(self, name)
        self.classroom = classroom
        self.mom = mom
        self.dad = dad


class Teacher(Person):

    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject


teach_1 = Teacher('МарьИванна', Subject('русский язык'))
teach_2 = Teacher('Варвара Петровна', Subject('математика'))
teach_3 = Teacher('Василий Петрович', Subject('физкультура'))
teach_4 = Teacher('Эльвира Константиновна', Subject('информатика'))
teach_5 = Teacher('Виталий Кузьмич', Subject('ОБЖ'))

classes = [Classroom('5a', [teach_1, teach_2, teach_3]), \
           Classroom('7b', [teach_1, teach_2, teach_3, teach_5]), \
           Classroom('11v', [teach_1, teach_2, teach_3, teach_4])]

school = School(classes)

stud_1 = Student('Петров Ф.П.', classes[0], Person('Петрова В.В.'), Person('Петров П.А.'))
stud_2 = Student('Пупкин В.П', classes[0], Person('Пупкина Ф.Ф.'), Person('Пупкин П.И.'))
stud_3 = Student('Иванова М.А.', classes[0], Person('Иванова В.Р.'), Person('Иванов А.Э.'))
stud_4 = Student('Буряк Э.З.', classes[1], Person('Буряк Е.К.'), Person('Буряк З.Ю.'))
stud_5 = Student('Сидорова К.О.', classes[1], Person('Сидорова Н.В.'), Person('Сидоров О.В.'))
stud_6 = Student('Хрущев К.А.', classes[1], Person('Хрущева П.Т.'), Person('Хрущев А.Н.'))
stud_7 = Student('Головач Е.А.', classes[2], Person('Юсупова Е.М.'), Person('Головач А.П.'))
stud_8 = Student('Самойлов А.А.', classes[2], Person('Самойлова Л.М.'), Person('Самойлов А.А'))
stud_9 = Student('Дубинкина О.С.', classes[2], Person('Дубинкина Н.Ф.'), Person('Дубинкин С.С.'))

students = [stud_1, stud_2, stud_3, stud_4, stud_5, stud_6, stud_7, stud_8, stud_9]

# 1. Получаем полный список всех классов школы

school.classlist()

# 2. Получаем список всех учеников в указанном классе

print('Введите класс: ')
answer = input()
for student in students:
    if answer == student.classroom.title:
        print(student.name)

# 3. Получаем список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)

print('Введите ФИО ученика: ')
answer = input()
found = False
for student in students:
    if answer == student.name:
        for teacher in student.classroom.teachers:
            print(teacher.subject.title)
        found = True
        break
if not found:
    print('Нет такого ученика.')

# 4. Узнаем ФИО родителей указанного ученика

print('Введите ФИО ученика: ')
answer = input()
for student in students:
    if answer == student.name:
        print(student.mom.name, student.dad.name)

# 5. Получаем список всех Учителей, преподающих в указанном классе

print('Введите класс: ')
answer = input()
for student in students:
    if answer == student.classroom.title:
        for teacher in student.classroom.teachers:
            print(teacher.name)
        break
        
        
"""Задание выполнено в соответствии со структурой "Ученик --> Класс --> Учителя --> Предметы", но логичнее
кажется "Учителя --> Предметы --> Класс --> Ученик"."""
