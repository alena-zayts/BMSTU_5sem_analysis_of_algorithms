from algs import *


def print_matrix(D, n_cities, message='Матрица:'):
    print(message)
    for i in range(n_cities):
        for j in range(n_cities):
            if D[i][j] != INF:
                print("%3d" % D[i][j], end=' ')
            else:
                print("INF", end=' ')
        print()


def tests_alg():
    def test_alg(D, n_cities, expected_answ, expected_way):
        print_matrix(D, n_cities)
        print(f'Ожидаемый результат:\n '
              f'{expected_answ}, {expected_way}')
        print()

        answ_full, way_full = full_search(D, n_cities)
        print(f'Результат алгоритма полного перебора:\n '
              f'{answ_full}, {way_full}')
        print(f'Длина минимального пути совпала с ожидаемой? - {answ_full == expected_answ}')
        print()

        answ_ant, way_ant = ant_search(D, n_cities)
        print(f'Результат муравьиного алгоритма:\n '
              f'{answ_ant}, {way_ant}')
        print(f'Длина минимального пути совпала с ожидаемой? - {answ_ant == expected_answ}')
        print('\n\n')

    D1 = [[0, 3, 4, 7],
          [3, 0, 3, 7],
          [4, 3, 0, 7],
          [7, 7, 7, 0]]
    n_cities1 = len(D1)
    expexcted_answ1 = 20
    expexcted_way1 = [0, 1, 2, 3, 0]

    D2 = [[0, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1],
          [1, 1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 0]]
    n_cities2 = len(D2)
    expexcted_answ2 = 6
    expexcted_way2 = [5, 4, 3, 2, 1, 0, 5]

    D3 = [[0, 1, INF, 4],
          [1, 0, 2, INF],
          [INF, 2, 0, 3],
          [4, INF, 3, 0]]
    n_cities3 = len(D3)
    expexcted_answ3 = 10
    expexcted_way3 = [0, 1, 2, 3, 0]

    test_alg(D1, n_cities1, expexcted_answ1, expexcted_way1)
    test_alg(D2, n_cities2, expexcted_answ2, expexcted_way2)
    test_alg(D3, n_cities3, expexcted_answ3, expexcted_way3)


if __name__ == '__main__':
    tests_alg()
    n = int(input('Введите количество городов: '))
    print('Введите матрицу смежности:')
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1):
            print("%3d" % D[i][j], end=' ')
        if i != n - 1:
            rest = list(map(float, input().split()))
            for j in range(i + 1, n):
                D[i][j] = rest[j - i - 1]
                D[j][i] = rest[j - i - 1]
    print()
    alpha = float(input('Введите параметр alpha: '))
    po = float(input('Введите параметр po: '))
    tmax = int(input('Введите параметр tmax: '))

    print_matrix(D, n, message='Матрица смежности: ')
    res, way = full_search(D, n)
    print(f'Алгоритм полного перебора: ответ={res}, путь={way}')
    res, way = ant_search(D, n, alpha, po, tmax)
    print(f'Муравьиный алгоритм: ответ={res}, путь={way}')
