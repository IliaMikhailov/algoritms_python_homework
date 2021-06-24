import random


def new_arr(l):
    return [random.randint(-100, 100) for i in range(l)]

def sort_bubble(arr):
    n = 1
    if len(arr) == 1:
        return arr
    while n < len(arr):
        flag = True # для улучшения алгоритма можно добавить переменную флаг
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = False
        if flag: # если перестановки были это значит, что массив ещё не отсортирован, если нет, то цикл завершится
            return arr
        n += 1
    return arr

x = new_arr(10)
print(x)
print(sort_bubble(x))


