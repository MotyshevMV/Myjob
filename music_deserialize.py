# 2: Создать модуль music_deserialize.py.  В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. # Получить объект — словарь из предыдущего задания.


import json
import pickle

with open('group.json', 'r') as f:
    print('Содержимое файла group.json')
    print(f.read())
with open('group.json', 'r') as f:
    my_favourite_group = json.load(f)
print('Результат десериализации содержимого файла group.json')
print(my_favourite_group)
with open('group.pickle', 'rb') as f:
    print('Содержимое файла group.pickle')
    print(f.read())
with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)
print('Результат десериализации содержимого файла group.pickle')
print(my_favourite_group)