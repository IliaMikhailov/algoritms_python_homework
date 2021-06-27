# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.
import random


def new_array(l):  # создание случайного массива в диапазоне [0;50)
    return [random.randint(0, 50) for i in range(l)]


def sort_merge(new_arr):  # функция для "дробления исходного массива на подмассивы"
    if len(new_arr) < 2:
        return new_arr[:]
    else:
        center = int(len(new_arr) / 2)
        left = sort_merge(new_arr[:center])
        right = sort_merge(new_arr[center:])
        return merge(left, right)


def compare(x, y):  # функция для выбора какое из значений мы занесём в результат в функции merge
    if x > y:
        return True
    else:
        return False


def merge(left, right):  # функция для слияния раздробленных массивов обратно в целый
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # первым циклом выбираем значения из двух ранее отсортированных массивов
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left): # если в одном из двух массивов остались значения, то вносим в результат оставшиеся значения
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


x = new_array(10)
print(x)
print(sort_merge(x))
