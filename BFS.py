# Поиск в ширину
from collections import deque
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# Условная функция проверки яв-ся ли человек продавцом манго
def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # Создание очереди(двусторонняя очередь "дека")
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += graph[name]
    # Список уже проверенных людей
    searched = []
    while search_queue:
        person = search_queue.popleft()  # Извлекает первого человека в очереди
        if not person in searched:  # Если нет в списке проверенных
            if person_is_seller(person):  # яв-ся ли продавцом
                print(person, ' is mango seller!!!')
                return True
            else:
                search_queue += graph[person]  # добавляет всех друзей в очередь
                searched.append(person)  # добавляет к проверенным
    return False


search('you')

# Задача найти кратчайшее расстояние
way = dict()
way['A'] = ['B', 'C']
way['B'] = ['E', 'D']
way['C'] = ['D']
way['E'] = ['G', 'I']
way['D'] = ['F']
way['G'] = ['FIN']
way['I'] = ['FIN']
way['F'] = ['I']


# Непонятно, выдает кол-во попыток которые он сделал
def go_fin(point):
    go_queue = deque()
    go_queue += way[point]
    searched_point = []
    attempt = 0
    while go_queue:
        attempt += 1
        x = go_queue.popleft()
        if not x in searched_point:
            if x == 'FIN':
                print('Finish')
                return attempt
            else:
                go_queue += way[x]
                searched_point.append(x)
    return None

print(go_fin('A'))