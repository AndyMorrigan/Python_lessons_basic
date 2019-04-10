__author__ = 'Быцкевич Анна Викторовна'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

listoffruits = ["яблоко", "банан", "киви", "арбуз"]
max_length = 0
# короткий путь max_length = len(max(listoffruits, key = len))

for fruit in listoffruits:
    max_length = (len(fruit) if len(fruit) > max_length else max_length)

for index, fruit in enumerate(listoffruits):
    print("{number}. {blanks}{item}".format(number = index + 1,
                                            blanks = " " * (max_length - len(fruit)),
                                            item = fruit))

print("_" * 20)
print()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

list1 = [random.randint(1, 20) for x in range(10)]
list2 = [random.randint(1, 20) for x in range(10)]
print("List 2: ", list2)
print("List 1: ", list1)

for element_in_2 in list2:
    for index, element_in_1 in enumerate(list1):
        if element_in_1 == element_in_2:
            list1.pop(index)

print("New List 1: ", list1)

print("_" * 20)
print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list = [random.randint(1, 20) for x in range(10)]
new_list = []

for element in list:
    if element % 2 == 0:
        new_list.append(element / 4)
    else:
        new_list.append(element * 2)

print("Старый список: ", list)
print("Новый список: ", new_list)
