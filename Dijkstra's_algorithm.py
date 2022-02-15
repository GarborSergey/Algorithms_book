# Алгоритм Дейкстры
# см. картинку Алгоритм Дейкстры
# Для реализации этого алгоритма понадобятся три хэш таблицы
# Таблица графа содержит узлы и их отношения друг к другу(веса ребер)
graph = dict()
# словари в словаре
graph['start'] = {}
graph['a'] = {}
graph['b'] = {}
graph['finish'] = {}  # У конечного узла нет соседей
# Веса ребер графа
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a']['finish'] = 1
graph['b']['a'] = 3
graph['b']['finish'] = 5

print(graph)

# Таблица для хранения стоимости всех узлов
# представление бесконечности
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'finish': infinity}

print(costs)

# Таблица для родителей
parents = {'a': 'start', 'b': 'start', 'finish': None}

print(parents)

# Список обработанных узлов, чтобы не зациклить
processed = []


# Функция по нахождению узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # Проход по всем узлам(ключам словаря)
        cost = costs[node]
        # Если этот узел с наименьшей стоимостью из всех проверенных и он не был обработан
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # Назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
print(node)
while node is not None:  # Пока не пройдем все узлы
    cost = costs[node]
    neighbors = graph[node]  # Достает словарь из словаря
    for n in neighbors.keys():  # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # Если к соседу можно добраться быстрее чем через текущий узел
            costs[n] = new_cost  # Обновляет стоимость для этого узла
            parents[n] = node  # Этот узел становится родителем для соседа
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(graph)
print(costs)
print(parents)
print(processed)