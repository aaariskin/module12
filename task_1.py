print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


def summa_n(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    print(f'Я знаю, что сумма чисел от 1 до {number} равна {result}')

number = int(input('Введите число: '))
summa_n(number)
