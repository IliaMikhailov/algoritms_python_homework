# Определить, какое число в массиве встречается чаще всего.
import random
import sys

def new_mas(l):
    return [random.randint(0, 5) for i in range(l)]

def mas_cycle(l_mas):
    mas_1 = new_mas(l_mas)
    max_count = 0
    max_number_index = 0
    for i in range(len(mas_1)):
        count = 0
        number = mas_1[i]
        for j in range(len(mas_1)):
            if mas_1[j] == number:
                count += 1
        if count > max_count:
            max_count = count
            max_number_index = i
    print(f'память затраченная на массив - {sys.getsizeof(mas_1)}')
    print(f'память затраченная на переменные max count - {max_count} max_number_index - {max_number_index}')
    return mas_1[max_number_index], max_count

# "lesson_4_task_1_cycle.mas_cycle(15)"
# 1000 loops, best of 5: 29.5 usec per loop
# "lesson_4_task_1_cycle.mas_cycle(50)"
# 1000 loops, best of 5: 170 usec per loop
# "lesson_4_task_1_cycle.mas_cycle(100)"
# 1000 loops, best of 5: 561 usec per loop
# "lesson_4_task_1_cycle.mas_cycle(500)"
# 1000 loops, best of 5: 12.8 msec per loop

def use_set(l_mas):
    mas_3 = new_mas(l_mas)
    uniks = set(mas_3)
    x = -1
    max_item = 0
    for item in uniks:
        if mas_3.count(item) > x:
            x = mas_3.count(item)
            max_item = item
    print(f'память затраченная на массив - {sys.getsizeof(mas_3)}')
    print(f'память затраченная на множество - {sys.getsizeof(uniks)}')
    return max_item, x

# "set_4.use_set(10)"
# 1000 loops, best of 5: 11.5 usec per loop
# "set_4.use_set(50)"
# 1000 loops, best of 5: 51.2 usec per loop
# "set_4.use_set(100)"
# 1000 loops, best of 5: 100 usec per loop
# "set_4.use_set(500)"
# 1000 loops, best of 5: 501 usec per loop

def dict_use(l_mas):
    mas_2 = new_mas(l_mas)
    dict = {}
    for item in mas_2:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    for key in dict.keys():
        if dict[key] == max(dict.values()):
            print(f'память затраченная на словарь - {sys.getsizeof(dict)}')
            print(f'память затраченная на список - {sys.getsizeof(mas_2)}')
            return key, max(dict.values())

# "dict_4.dict_use(10)"
# 1000 loops, best of 5: 12.6 usec per loop
# "import dict_4" "dict_4.dict_use(50)"
# 1000 loops, best of 5: 53.5 usec per loop
# "dict_4.dict_use(100)"
# 1000 loops, best of 5: 107 usec per loop
# "dict_4.dict_use(500)"
# 1000 loops, best of 5: 518 usec per loop

print(mas_cycle(1000))
print(use_set(1000))
print(dict_use(1000))
print(sys.version, sys.platform)
# При длине списка в 1000 значений
# цикл - 8856 + 176 + 5
# множество - 8856 + 728
# словарь - 8856 + 360

# При длине списка в 100 значений
# цикл - 920 + 20 + 3
# множество - 920 + 728
# словарь - 920 + 360

# При длине списка в 10 значений
# цикл - 184 + 4 + 3
# множество - 184 + 728
# словарь - 184 + 360

"""Общий вывод: Способ решения со словарём выигрывает по объёму памяти, а также сравним по быстродействию со множеством"""

