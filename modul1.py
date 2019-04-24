#1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py). В нем напишите функцию,
# создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код. Затем создайте вторую функцию,
# удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os


def add_dir(path_var, number_var):
    for i in range(1,number_var+1):
        new_path = os.path.join(os.getcwd(),f'{path_var}_{i}')
        os.mkdir(new_path)

if __name__ == '__main__':
    path = 'dir'
    add_dir(path, 9)

def remove_dir(path_var, number_var):
    for i in range(1,number_var+1):
        new_path = os.path.join(os.getcwd(),f'{path_var}_{i}')
        os.rmdir(new_path)


if __name__ == '__main__':
    path = 'dir'
    remove_dir(path, 9)

