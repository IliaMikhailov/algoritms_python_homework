'''
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''


# создаём граф, где все вершины связаны друг с другом, но без петель
def create_graph(l):
    return {i + 1: [j + 1 for j in range(l) if i != j] for i in range(l)}


def depth_first_search(graph, start, end, visited=None, way=None):
    if visited == None:
        visited = {i + 1: False for i in range(end + 1)}
        way = []
    visited[start] = True
    way.append(start)
    for w in graph[start]:
        if not visited[w]:
            depth_first_search(graph, w, end, visited, way)
    return way


a = 5  # количество вершин графа
new_graph = create_graph(a)
print(new_graph)
print(depth_first_search(new_graph, 1, a))
# Для интереса ниже добавил другой граф, где будет более наглядно виден обход в глубину
#primer = {1: [2, 3], 2: [4], 3: [5], 4: [7], 5: [6], 6: [], 7: []}
#print(depth_first_search(primer, 1, max(primer)))
