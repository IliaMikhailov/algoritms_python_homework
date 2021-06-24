import random


def new_array(l):  # создание случайного массива в диапазоне [0;50)
    return [random.randint(0, 50) for i in range(l)]

# медианой массива с n элементами называется элемент, значение которого меньше или равно половины n элементов и больше другой половины
def find_mediane(arr):
    for i in arr:
        count_more = 0
        count_less = 0
        count_equal = 0
        for h in arr:
            if i == h:
                count_equal += 1
            elif i > h:
                count_more += 1
            else:
                count_less += 1
        # после подсчёта количество меньших, больших  равных элементов сравниваем эти значения
        if count_equal % 2 == 0 and (count_less == count_more + 1 or count_less + 1 == count_more):
            return i
        elif count_equal == 1 and count_less == count_more:
            return i
        elif count_equal % 2 != 0 and (count_less == count_more + count_equal or count_less + count_equal == count_more):
            return i
    return f'такого числа нету'


x = new_array(25)
print(x)
print(find_mediane(x))
x.sort()
print(x)
print(x[len(x) // 2])