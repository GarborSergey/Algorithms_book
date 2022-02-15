# Жадные алгоритмы получают решение близкое к оптимальному
# выбрать радиостанции

# множества не содержат дубликатов
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])  # Переданный массив преобразуется в множество

# словарь станциий
stations = {'kone': set(['id', 'nv', 'ut']),
           'ktwo': set(['id', 'wa', 'mt']),
           'kthree': set(['or', 'nv', 'ca']),
           'kfour': set(['nv', 'ut']),
           'kfive': set(['az', 'ca'])
           }

final_station = set()  # Оптимальный выбор станций

while states_needed:  # пока штаты не закончатся
    best_station = None  # Станция, которая обслуживает больше всего штатов
    station_covered = set()  # Множество со всеми штатами обслуживающееся это станцией
    for station, station_for_station in stations.items():  # Прибирает все станции и находит лучшую
        covered = states_needed & station_for_station  # Пересечение множеств
        if len(covered) > len(station_covered):
            best_station = station
            station_covered = covered
        final_station.add(best_station)  # добавить в выходной список станцию
        states_needed -= station_covered  # удалить из множества штатов штаты, которые обслуживает добавленная станция

print(final_station)
