from random import random, shuffle

INF = 1e10
EPS = 1e-5

ALPHA = 0.5
PO = 0.5
TMAX = 100

def count_way_lenth(D, visited_cities):
    lk = 0

    for l in range(1, len(visited_cities)):
        i = visited_cities[l - 1]
        j = visited_cities[l]
        lk += D[i][j]

    return lk


def ant_search(D, n_cities, alpha=ALPHA, po=PO, tmax=TMAX):
    Q = 0
    for j in range(n_cities):
        for j in range(n_cities):
            if D[j][j] < INF:
                Q += D[j][j]
    beta = 1 - alpha

    # Инициализация ребер — присвоение видимости eta
    # и начальной концентрации феромона.
    eta = [[0 for i in range(n_cities)] for j in range(n_cities)]
    tau = [[0 for i in range(n_cities)] for j in range(n_cities)]
    for i in range(n_cities):
        for j in range(n_cities):
            if j != i:
                eta[i][j] = 1 / D[i][j]
                tau[i][j] = 2 * EPS

    min_way_length = INF

    # Цикл по времени жизни колонии
    for t in range(tmax):
        # Размещение муравьев в случайно выбранные города без совпадений.
        l = list(range(n_cities))
        shuffle(l)
        visited_cities = [[i] for i in range(n_cities)]

        #  Цикл по всем муравьям
        for k in range(n_cities):
            # Построить маршрут
            while len(visited_cities[k]) != n_cities:
                P_ch = [0 for i in range(n_cities)]
                for j in range(n_cities):
                    if j not in visited_cities[k]:
                        i = visited_cities[k][-1]
                        P_ch[j] = (tau[i][j] ** alpha) * (eta[i][j] ** beta)

                P_zn = sum(P_ch)
                for j in range(n_cities):
                    P_ch[j] /= P_zn

                coin = random()
                summ, j = 0, 0
                while summ < coin:
                    summ += P_ch[j]
                    j += 1
                visited_cities[k].append(j - 1)

            visited_cities[k].append(visited_cities[k][0])
            way_length = count_way_lenth(D, visited_cities[k])

            # Выбрать лучшее решение
            if way_length < min_way_length:
                min_way_length = way_length
                min_way = visited_cities[k]

        # Обновление следов феромона на ребрах
        for i in range(n_cities):
            for j in range(i):
                delta_tau = 0
                # подсчет добавления
                for k in range(n_cities):
                    way_length = count_way_lenth(D, visited_cities[k])
                    for m in range(1, len(visited_cities[k])):
                        if (visited_cities[k][m], visited_cities[k][m - 1]) in ((i, j), (j, i)):
                            delta_tau += Q / way_length
                            break

                # испарение и добавление
                tau[i][j] = tau[i][j] * (1 - po) + delta_tau
                if tau[i][j] < EPS:
                    tau[i][j] = EPS

    return min_way_length, min_way


def full_search(D, n_cities):
    # генератор перестановок
    def next_set(a, n):
        # инициализация
        if not a:
            for i in range(n):
                a.append(i)
            return True

        # просмотреть текущую перестановку справа налево и при этом следить за тем,
        # чтобы каждый следующий элемент перестановки был не более чем предыдущий.
        j = n - 2
        while j != -1 and a[j] >= a[j + 1]:
            j -= 1
        if j == -1:
            return False  # больше перестановок нет

        # cнова просмотреть пройденный путь справа налево пока не дойдем до первого числа,
        # которое больше чем отмеченное на предыдущем шаге.
        k = n - 1
        while a[j] >= a[k]:
            k -= 1
        # поменять местами два полученных элемента.
        a[j], a[k] = a[k], a[j]

        # сортируем оставшуюся часть последовательности
        l = j + 1
        r = n - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return True

    min_way_length = INF
    min_way = None
    cur_way = []

    while next_set(cur_way, n_cities):
        cur_way_lenth = count_way_lenth(D, cur_way + [cur_way[0], ])
        if cur_way_lenth < min_way_length:
            min_way_length = cur_way_lenth
            min_way = cur_way

    return min_way_length, min_way + [min_way[0]]