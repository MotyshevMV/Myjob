
# 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
#
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.


import modul1
from modul2 import random_choice

modul1.add_dir('dir',4)
modul1.remove_dir('dir',2)
list1=[25, 35, 79, 22, 11]
print(random_choice(list1))
list2=[1, 2, 4, 6, 8, 3]
print(random_choice(list2))
