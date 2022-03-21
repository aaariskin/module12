print('Задача 3. Апгрейд калькулятора')


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.
def summ_num(number):
    result = 0
    for char in number:
        result += int(char)
    print('Сумма цифр равна', result)


def max_number(number):
    max = 0
    for i in number:
        if i > max:
            max = i
    print('Максимальная цифра равна', max)


def min_number(number):
    min = 0
    for i in number:
        if i < min:
            min = i
    print('Максимальная цифра равна', min)


while True:
    number = int(input('Введите число: '))
    action = int(
        input(
            'Выберите действие:\n1 сумма цифр\n2 вывести максимальную цифру\n3 Вывести минимальную цифру\n0 выход\n'
        ))
    if action == 0:
        break
    elif action == 1:
        summ_num(number)
    elif action == 2:
        max_number(number)
    elif action == 3:
        min_number(number)