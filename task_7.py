print('Задача 7. Опять?')

# Вы снова встретились со своим старым другом,
# который был безмерно благодарен вам за то,
# что вы помогли ему сдать задачу тому преподавателю.
#
# Вот только друг всё равно выглядел довольно грустным.
# Спросив в чём дело, друг взорвался эмоциями и рассказал,
# что теперь препод попросил написать функцию нахождения минимального числа
# без использования условного оператора, циклов и функции min.
#
# Конечно же, вы решили снова помочь бедняге.
# Напишите для него такую программу.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второее число: '))

lst = [first_number, second_number]
lst_num = list(enumerate(lst, 0))

result = first_number + second_number - (max(lst_num, key=lambda i: i[1]))[1]
print('Наименьшее число: ', result)
