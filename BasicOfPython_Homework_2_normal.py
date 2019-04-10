__author__ = 'Быцкевич Анна Викторовна'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random

list_task1 = [random.randint(-25, 25) for x in range(20)]
#list_task1 = [2, -5, 8, 9, -25, 25, 4]
new_list_task1 = []

for element in list_task1:
    if element > 0:
        if (element ** (1/2)).is_integer():
            new_list_task1.append(int(element ** (1/2)))

print(list_task1)
print(new_list_task1)

print("_" * 20)
print()

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


#import locale
import calendar

#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
date = input("Введите дату: ")
date = [int(x) for x in date.split(".")]
months = ["", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа",
          "сентября", "октября", "ноября", "декабря"]
day_numbers = ["", "первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое",
               "десятое", "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое",
               "шестнадцатое", "семнадцатое", "восемьнадцатое", "девятнадцатое", "двадцатое", "двадцать первое",
               "двадвацть второе", "двадцать третье", "двадцать четвертое", "двадцать пятое", "двадцать шестое",
               "двадцать седьмое", "двадцать восьмое", "двадцать девятое", "тридцатое", "тридцать первое"]

print("{number} {month} {year} года".format(number=day_numbers[date[0]],
                                            month=months[date[1]],
                                            year=date[2]))
#print("{number} {month} {year} года".format(number=calendar.day_name[0],
#                                           month=calendar.month_name(date[1]),
#                                           year=date[2]))
# Закомментированный код выдает ошибки по типу TypeError: 'localized_month' object is not callable, если поможете разобраться, буду благодарна


print("_" * 20)
print()

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

#import random - уже импортирован в 1 задании
n = int(input("Введите количество значений списка: "))
list_task3 = []

for x in range(n):
    list_task3.append(random.randint(-100, 100))

print(list_task3)

# или одной строкой list_task3 = [random.randint(-100, 100) for x in range(n)]

print("_" * 20)
print()

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

from collections import Counter
list_task4 = [random.randint(0, 10) for x in range(12)]
#list_task4 = [1 , 2, 4, 5, 6, 2, 5, 2]
new_list_task4a = []
new_list_task4b = []

new_list_task4a = list(set(list_task4))

count = Counter(list_task4)
for element in list_task4:
    if count[element] == 1:
        new_list_task4b.append(element)

print(list_task4)
print(new_list_task4a)
print(new_list_task4b)
