#2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random

def random_choice(list_var):
    if len(list_var) == 0:
        return None
    else:
        return random.choice(list_var)

if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    print(random_choice(list1))
    print(random_choice(list2))