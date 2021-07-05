# 1. Определить количество подстрок в строке

def count_str(s):
    new_set = set()
    for i in range(len(s)):
        for j in range(len(s) - 1 if i == 0 else len(s), i, -1):
            new_set.add(hash(s[i:j]))
    return len(new_set)

s = str(input("Введите строку S: "))
print("Количество различных подстрок в этой строке:", count_str(s))