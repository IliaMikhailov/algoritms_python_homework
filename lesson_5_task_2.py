# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.

from collections import defaultdict


def number_from_16_to_10(list_number):
    dict_16_10 = defaultdict()
    str_for_dict = '0123456789ABCDEF'
    for i in str_for_dict:
        dict_16_10[i] = str_for_dict.index(i)
    number = 0
    for i in list_number:
        number += dict_16_10[i] * 16 ** (len(list_number) - list_number.index(i) - 1)
    return number


def number_from_10_to_16(number):
    dict_10_16 = defaultdict(int)
    str_for_dict = '0123456789ABCDEF'
    for i in range(len(str_for_dict)):
        dict_10_16[i] = str_for_dict[i]
    result = []
    for i in range(len(str(number))):
        result.append(dict_10_16[number % 16])
        number = number // 16
        if number < 16:
            result.append(dict_10_16[number % 16])
            break
    result.reverse()
    return result


a = ['C', '4', 'F']
b = ['A', '2']
a_10 = number_from_16_to_10(a)
b_10 = number_from_16_to_10(b)
print(number_from_10_to_16(a_10 + b_10))
print(number_from_10_to_16(a_10 * b_10))
