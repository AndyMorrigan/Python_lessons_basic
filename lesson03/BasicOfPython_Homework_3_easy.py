# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    splitbydot = [x for x in str(number).split('.')]
    beforedot = len(splitbydot[0])
    number = splitbydot[0] + splitbydot[1]
    while len(number) > (ndigits + beforedot):
        deciminal = int(number) % 10
        number = int(number) // 10
        if deciminal == 0:
            number = str(number)
        elif deciminal >= 5:
            number = str(number + 1)
        else:
            number = str(number - 1)
    number = float(number) / (10 ** ndigits)
    return number

print(my_round(2.1234567, 5))
print(my_round(102.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.9999967, 0))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    flag = None
    ticket_number = str(ticket_number)
    firstsum = int(ticket_number[0]) + int(ticket_number[1])
    secondsum = int(ticket_number[-1]) + int(ticket_number[-2])
    if firstsum == secondsum:
        flag = "You lucky!"
    else:
        flag = "Maybe next time"
    return flag


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
