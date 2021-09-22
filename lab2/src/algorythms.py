from copy import deepcopy
from time import process_time

debug = False


def standart_mult(a, b, c, m, n, q):
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c


def vinograd_usual_mult(a, b, c, m, n, q):
    mulh = [0 for i in range(m)]
    for i in range(m):
        for k in range(n//2):
            mulh[i] = mulh[i] + a[i][k * 2] * a[i][k * 2 + 1]

    mulv = [0 for i in range(q)]
    for i in range(q):
        for k in range(n//2):
            mulv[i] = mulv[i] + b[k * 2][i] * b[k * 2 + 1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = -mulh[i] - mulv[j]
            for k in range(n//2):
                c[i][j] = c[i][j] + (a[i][k * 2] + b[2 * k + 1][j]) * (a[i][2 * k + 1] + b[2 * k][j])

    if n % 2:
        for i in range(m):
            for j in range(q):
                c[i][j] = c[i][j] + a[i][n - 1] * b[n - 1][j]

    return c


# 1) замена k < n//2, k++, *2 в цикле  на  k < n, k += 2, ничего. При этом заранее n-=1 и в 4 действии отсутствие -1
# 2) замена всех a = a +.. на a+=
# 3) замена в mulh += на -= и тогда c[i][j] = mulh[i] - mulv[j]
def vinograd_optimized_mult(a, b, c, m, n, q):
    n -= 1
    mulh = [0 for i in range(m)]
    for i in range(m):
        for k in range(0, n, 2):
            mulh[i] -= a[i][k] * a[i][k + 1]

    mulv = [0 for i in range(q)]
    for i in range(q):
        for k in range(0, n, 2):
            mulv[i] += b[k][i] * b[k + 1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = mulh[i] - mulv[j]
            for k in range(0, n, 2):
                c[i][j] += ((a[i][k] + b[k + 1][j]) * (a[i][k + 1] + b[k][j]))

    if (n % 2) == 0:
        for i in range(m):
            for j in range(q):
                c[i][j] += a[i][n] * b[n][j]

    return c


def print_matrix(m):
    for line in m:
        print(line)


def answer_user():
    if not debug:
        print('Введите размерность первой матрицы.')
        m = int(input('m: '))
        n = int(input('n: '))
        print('Введите первую матрицу построчно, через пробелы')
        a = []
        for i in range(m):
            a.append(list(map(int, input().split())))
            if len(a[-1]) != n:
                print('Ошибка')
                return
        print()

        print('Введите размерность второй матрицы.')
        nn = int(input('n: '))
        q = int(input('q: '))
        if n != nn:
            print('Ошибка: количество строк в первой матрице должно быть равно количеству столбцов во второй матрице')
            return
        print('Введите вторую матрицу построчно, через пробелы')
        b = []
        for i in range(nn):
            b.append(list(map(int, input().split())))
            if len(b[-1]) != q:
                print('Ошибка')
                return
        print()

    else:
        m = 2
        n = 2
        q = 4
        a = [[1, 2],
             [3, 4]]
        b = [[1, 2, 3, 4],
             [2, 3, 4, 5]]

    c = [[0 for i in range(q)] for j in range(m)]


    print(f'\nСтандартный алгоритм')
    beg = process_time()
    answer = standart_mult(a, b, deepcopy(c), m, n, q)
    end = process_time()
    print('Ответ:')
    print_matrix(answer)
    print(f'Время: {end-beg}')

    print(f'\nАлгоритм Винограда')
    beg = process_time()
    answer = vinograd_usual_mult(a, b, deepcopy(c), m, n, q)
    end = process_time()
    print('Ответ:')
    print_matrix(answer)
    print(f'Время: {end-beg}')

    print(f'\nОптимизированный алгоритм Винограда')
    beg = process_time()
    answer = vinograd_optimized_mult(a, b, deepcopy(c), m, n, q)
    end = process_time()
    print('Ответ:')
    print_matrix(answer)
    print(f'Время: {end-beg}')

    print()
    print()


if __name__ == '__main__':
    while True:
        print()
        answer_user()


