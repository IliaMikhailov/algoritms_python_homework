# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict

number_factories = int(input(" Введите количество заводов для ввода"))
a = defaultdict(dict)
main_profit = 0
for i in range(number_factories):
    name = input('Введите название завода')
    money1 = int(input('Введите прибыль за 1-ый квартал'))
    money2 = int(input('Введите прибыль за 2-ой квартал'))
    money3 = int(input('Введите прибыль за 3-й квартал'))
    money4 = int(input('Введите прибыль за 4-й квартал'))
    new_list = {name: [money1, money2, money3, money4]}
    a[i] = new_list
    main_profit += money1 + money2 + money3 + money4
main_profit /= number_factories
for i in range(number_factories):
    for key in a[i]:
        if sum(a[i][key]) > main_profit:
            print(f'Завод {key} имеет прибыль выше средней')
        else:
            print(f'Завод {key} имеет прибыль ниже средней')
print(f'Средняя прибыль всех предприятий {main_profit}')
