# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for a in range(1, 10):
    dir_name = 'dir_{}'.format(a)
    new_dirs = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(new_dirs)
    except FileExistsError:
        print('Директория уже существует')

for a in range(1, 10):
    dir_name = 'dir_{}'.format(a)
    new_dirs = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(new_dirs)
    except FileExistsError:
        print('Директория отсутствует')

# Задача-2:
# Напишите скрипт отображающий папки текущей директории

for root, dirs, files in os.walk(os.getcwd()):
    print(dirs)

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

import sys
import shutil

curr_file = str(sys.argv)
curr_file = curr_file[2:-2]
copy_file = curr_file + '-copy'
shutil.copy(curr_file, copy_file)
