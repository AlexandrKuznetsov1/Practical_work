

# Задание выполнено после обновления платформы с учетом полученных знаний до модуля 8

# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.

# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else),
# которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0


print('Пожалуйста, введите поочереди три целых числа. Я скажу Вам сколько одинаковых:')
while 1:
    try:
        first = int(input('Введите значение first:  '))
        second = int(input('Введите значение second:  '))
        third = int(input('Введите значение third:  '))
        break
    except ValueError as exc:
        print(f"Недопустимое значение {exc}, \nПожалуйста повторите ввод.")
        continue

if isinstance(first, int) and isinstance(second, int) and isinstance(third, int):
    if first == second == third:
        a = 3
        print(f'Вы ввели {a} равных числа')
    if first == second != third or first == third != second or second == third != first:
        b = 2
        print(f'Вы ввели {b} равных числа')
    else:
        if first != second or first != third or second != third:
            print("Равных чисел среди введенных нет,- результат '0'")




