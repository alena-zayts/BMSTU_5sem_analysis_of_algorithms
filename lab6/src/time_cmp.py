from algs import *
from random import randint, choice
from time import process_time
import matplotlib.pyplot as plt


def generate_matrix_one_way(n):
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
            if i != j:
                if i == j + 1:
                    D[i][j] = i + j + 1
                    D[j][i] = i + j + 1
                else:
                    D[i][j] = INF
                    D[j][i] = INF
    D[0][n - 1] = n
    D[n - 1][0] = n
    return D


def generate_matrix_all_same(n):
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
            if i != j:
                D[i][j] = 3
                D[j][i] = 3
    return D


def generate_matrix_random(n):
    D = generate_matrix_one_way(n)
    for i in range(n):
        for j in range(i):
            if D[i][j] == INF:
                rand_num = randint(1, 10)
                res = choice([rand_num, INF])
                D[i][j] = res
                D[j][i] = res
    return D


path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab6/report/inc/img/'
time_file = path + 'times.txt'
filename_all = path + 'time_all.png'


def time_cmp():
    n_max = 11
    n_repeats = 6
    ns = list(range(3, n_max))

    time_fulls = []
    time_ant_rands = []
    time_ant_one_ways = []
    time_ant_all_sames = []
    for n in ns:
        time_full = 0
        time_ant_rand = 0
        time_ant_one_way = 0
        time_ant_all_same = 0

        D_rand = generate_matrix_random(n)
        D_all_same = generate_matrix_all_same(n)
        D_one_way = generate_matrix_one_way(n)
        for i in range(n_repeats):
            print(i)
            start = process_time()
            answ, way = full_search(D_rand, n)
            end = process_time()
            time_full += (end - start)

            start = process_time()
            answ, way = ant_search(D_rand, n)
            end = process_time()
            time_ant_rand += (end - start)

            start = process_time()
            answ, way = ant_search(D_one_way, n)
            end = process_time()
            time_ant_one_way += (end - start)

            start = process_time()
            answ, way = ant_search(D_all_same, n)
            end = process_time()
            time_ant_all_same += (end - start)

        time_fulls.append(time_full / n_repeats)
        time_ant_rands.append(time_ant_rand / n_repeats)
        time_ant_one_ways.append(time_ant_one_way / n_repeats)
        time_ant_all_sames.append(time_ant_all_same / n_repeats)

        print(f'n={n}, time_fulls={time_fulls[-1]}, time_ant_rands={time_ant_rands[-1]},\n'
              f'time_ant_one_ways={time_ant_one_ways[-1]}, time_ant_all_sames={time_ant_all_sames[-1]}')

        with open(time_file, 'w') as f:
            f.write(' '.join(list(map(str, ns))) + '\n')
            f.write(' '.join(list(map(str, time_fulls))) + '\n')
            f.write(' '.join(list(map(str, time_ant_rands))) + '\n')
            f.write(' '.join(list(map(str, time_ant_one_ways))) + '\n')
            f.write(' '.join(list(map(str, time_ant_all_sames))) + '\n')

        # print_matrix(D_rand, n, message=f'D_rand, n={n}')
        # print_matrix(D_all_same, n, message=f'D_all_same, n={n}')
        # print_matrix(D_one_way, n, message=f'D_one_way, n={n}')


def draw_plot_all():
    with open(time_file, 'r') as f:
        ns = list(map(float, f.readline().split()))
        time_fulls = list(map(float, f.readline().split()))
        time_ant_rands = list(map(float, f.readline().split()))
        time_ant_one_ways = list(map(float, f.readline().split()))
        time_ant_all_sames = list(map(float, f.readline().split()))


    plt.xlabel('Количество городов')
    plt.xticks(ns)
    plt.ylabel('Время работы реализации (с)')
    plt.grid()

    plt.plot(ns, time_fulls, label='Полный перебор')
    plt.plot(ns, time_ant_rands, label='Муравьиный (случайная)')
    plt.plot(ns, time_ant_one_ways, label='Муравьиный (с одним путем)')
    plt.plot(ns, time_ant_all_sames, label='Муравьиный (с равными путями)')

    plt.legend(loc='best')
    plt.savefig(filename_all)


if __name__ == '__main__':
    time_cmp()
    draw_plot_all()
