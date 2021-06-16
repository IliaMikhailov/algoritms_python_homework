# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
import sys
def sum_progr(n):

    if n == 1:
        return 1
    else:
        return 1 + sum_progr(n - 1) / -2

# "lesson4_1.sum_progr(10)"
# 1000 loops, best of 5: 1.61 usec per loop
# "lesson4_1.sum_progr(50)"
# 1000 loops, best of 5: 8.57 usec per loop
# "lesson4_1.sum_progr(100)"
# 1000 loops, best of 5: 17.6 usec per loop
# "lesson4_1.sum_progr(500)"
# 1000 loops, best of 5: 100 usec per loop

def sum_list(l):
    new_list = [1, ]
    for i in range(1, l):
        new_list.append(new_list[i - 1] * (-0.5))
    print(f'список - {sys.getsizeof(new_list)}')
    return sum(new_list)
# "lesson4_1.sum_list(10)"
# 1000 loops, best of 5: 1.56 usec per loop
# "lesson4_1.sum_list(50)"
# 1000 loops, best of 5: 5.41 usec per loop
# "lesson4_1.sum_list(100)"
# 1000 loops, best of 5: 10.3 usec per loop
# "lesson4_1.sum_list(500)"
# 1000 loops, best of 5: 59.3 usec per loop

def sum_dict(l):
    sum_d = {0: 1, }
    if l in sum_d:
        return sum_d[l]
    else:
        for i in range(1, l):
            sum_d[i] = 1 + sum_d[i - 1] / -2
    print(f'словарь - {sys.getsizeof(sum_d)}')
    return sum_d[l - 1]

# "lesson4_1.sum_dict(10)"
# 1000 loops, best of 5: 1.86 usec per loop
# "lesson4_1.sum_dict(50)"
# 1000 loops, best of 5: 8.11 usec per loop
# "lesson4_1.sum_dict(100)"
# 1000 loops, best of 5: 16.1 usec per loop
# "lesson4_1.sum_dict(500)"
# 1000 loops, best of 5: 90.9 usec per loop

print(f'n - {sys.getsizeof(1000)}')
print(sum_list(1000))
print(sum_dict(1000))
print(sys.version, sys.platform)

# у sum_progr только 1 переменная n - весит она 28 при любых значениях
#список - 4216 при 500
#словарь - 18520 при 500
#список - 8856 при 1000
#словарь - 36960 при 1000
# 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] win32
"""В даннной программе из трёх решений я бы выбрал уже первое с рекурсией, так как 
1) быстродействие не сильно отличается от списка и словаря
2) достаточно маленький объём написанного кода, в котором просто разобраться
3) фиксированный объём памяти для хранения 1 переменной"""