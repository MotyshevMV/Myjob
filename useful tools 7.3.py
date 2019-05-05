# 4. Написать функцию, которая принимает на вход число от 1 до 100.
#Если число равно 13, функция поднимает исключительную ситуации ValueError,
#иначе возвращает введенное число, возведенное в квадрат.
#Далее написать основной код программы. Пользователь вводит число. Введенное
#число передаем параметром в написанную функцию и печатаем результат,
#который она вернула.
#Обработать возможность возникновения исключительной ситуации,
#которая поднимается внутри функции.


def func(number_var):
    try:
        if number_var == 13 or number_var < 1 or number_var > 100:
            raise ValueError
    except ValueError:
        return 'Мишаня, переделывай: '
    else:
        return number_var ** 2


number = int(input('Введите число: '))
print(func(number))


def magic_func(inp_value):
    if inp_value == 13:
        raise ValueError
    else:
        return inp_value ** 2


try:
    inp = int(input('Введите число: '))
    if 0 < inp < 101:
        print(magic_func((inp)))
    else:
        print('Число не подходит, Мишаня переделывай: ')
except ValueError:
    print('Все сломалось, работать не будет ')
