'''
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''
def create_graph(l):
    return [[0 if i >= j else 1 for j in range(l)] for i in range(l)]

def sum_graph(graph):
    result = 0
    for i in graph:
        result += sum(i)
    return result

n = 5 # количество друзей
new_graph = create_graph(n)
print(sum_graph(new_graph))