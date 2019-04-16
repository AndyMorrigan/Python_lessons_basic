# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fibonacci_list = []

    def recursion(index):
        if index >= 2:
            number = recursion(index - 1) + recursion(index - 2)
        else:
            number = index
        return number

    for index in range(n, m + 1):
        fibonacci_list.append(recursion(index))

    return fibonacci_list


# Попытка решить по формуле Бине дала ошибку, ответ не правильный, причину не поняла
# def fibonacci2(n, m):
#     fibonacci_list = []
#
#     def bine(number):
#         square5 = 5 ** (1 / 2)
#         phi = (1 + square5) / 2
#         minusphi = (1 - square5) / 2
#         formula = int((phi ** number) + (minusphi ** number) / square5)
#         return formula
#
#     for index in range(n, m + 1):
#         fibonacci_list.append(bine(index))
#
#     return fibonacci_list


print(fibonacci(1, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    length = len(origin_list)
    check = 0
    while check < length - 1:
        index = 0
        check = 0
        for element in origin_list:
            if index < length - 1:
                if element > origin_list[index + 1]:
                    replacement = origin_list[index + 1]
                    origin_list[index + 1] = element
                    origin_list[index] = replacement
                else:
                    check += 1
                index += 1
    return origin_list


print([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(function, iterables):
    new_list = []
    for element in iterables:
        if function(element):
            new_list.append(element)
    return new_list


print(list(filter(lambda x: x > 2, [1, 2, 5, 6, 0])))
print(my_filter(lambda x: x > 2, [1, 2, 5, 6, 0]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


