from random import *  # подключаем модуль random


def is_valid(num_check, lim1, lim2):  # Проверка корректности ввода:
    if num_check.isdigit():  # Ввод числа
        if lim1 <= int(num_check) <= lim2:  # Число целое и в диапазоне от 1 до 100 включительно
            return True  #
        else:
            return False
    return False


print('Добро пожаловать в числовую угадайку')  # Приветствие
limit1 = int(input('Нижняя граница: '))
limit2 = int(input('Верхняя граница: '))
rnd = randint(limit1, limit2)  # загадываем случайное число от 1 до 100 включительно
try_count = 0

while True:

    while True:
        num_input = str(input('Введите число: '))
        if not is_valid(num_input, limit1, limit2):
            print(f'А может быть все-таки введем целое число от {limit1} до {limit2}?')
        else:
            num = int(num_input)
            break

    if num > rnd:
        print('Ваше число больше загаданного, попробуйте еще разок')
        try_count += 1
    elif num < rnd:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        try_count += 1
    else:
        print('Вы угадали, поздравляем!')
        print(f'Количество попыток: {try_count+1}')
        again = str(input('Сыграем ещё раз? (Да - д , Нет - н): '))
        if again == 'д':
            try_count = 0
            rnd = randint(limit1, limit2)  # повторно загадываем случайное число от 1 до 100 включительно
            continue
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
