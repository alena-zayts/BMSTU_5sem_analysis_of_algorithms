from algs import *
#from time_cmp import generate_matrix_random, generate_matrix_one_way, diff
from random import randint, choices
from tests import print_matrix
from copy import copy
import pandas as pd

alphas = [0.1, 0.25, 0.5, 0.75, 0.9]
pos = copy(alphas)
tmaxs = [100, 200, 300, 400, 500]


small_diff = 10
big_diff = 1000
local_diff = 2
# diff = 30
n_cities = 9
file_i = 9

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab6/report/inc/img/'
#df_file = path + 'df3.xlsx'



def generate_matrix_one_way(n):   # local
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
            if i == j + 1:
                D[i][j] = small_diff - local_diff
                D[j][i] = small_diff - local_diff
            elif (i + j) % 4 == 0:
                D[i][j] = small_diff + local_diff
                D[j][i] = small_diff + local_diff
            else:
                D[i][j] = small_diff
                D[j][i] = small_diff
    D[0][n - 1] = small_diff - local_diff
    D[n - 1][0] = small_diff - local_diff
    return D


def generate_matrix_random(n):  # small
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
                rand_num = randint(1, small_diff)
                # res = choices([rand_num, INF], weights=[0.8, 0.2])[0]
                res = rand_num
                D[i][j] = res
                D[j][i] = res
    return D

def generate_matrix_all_same(n): # big
    D = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i):
                rand_num = randint(1, big_diff)
                # res = choices([rand_num, INF], weights=[0.8, 0.2])[0]
                res = rand_num
                D[i][j] = res
                D[j][i] = res
    return D


def make_table():
    df = pd.DataFrame(columns=['alpha', 'po', 'tmax', 'diff_all_same', 'diff_rand', 'diff_one_way', 'diff_sum'])

    D_rand = generate_matrix_random(n_cities)
    print_matrix(D_rand, n_cities, message='D_rand')

    D_one_way = generate_matrix_one_way(n_cities)
    print_matrix(D_one_way, n_cities, message='D_one_way')

    D_all_same = generate_matrix_all_same(n_cities)
    print_matrix(D_all_same, n_cities, message='D_all_same')

    answer_full_rand, _ = full_search(D_rand, n_cities)
    print('here')
    answer_full_one_way, _ = full_search(D_one_way, n_cities)
    print('here')
    answer_full_all_same, _ = full_search(D_all_same, n_cities)
    print('here')

    for alpha in alphas:
        for po in pos:
            for tmax in tmaxs:
                answer_ant_rand, _ = ant_search(D_rand, n_cities, alpha, po, tmax)
                answer_ant_one_way, _ = ant_search(D_one_way, n_cities, alpha, po, tmax)
                answer_ant_all_same, _ = ant_search(D_all_same, n_cities, alpha, po, tmax)

                results = {'alpha': alpha, 'po': po, 'tmax': tmax,
                           'diff_rand': answer_ant_rand - answer_full_rand,
                           'diff_one_way': answer_ant_one_way - answer_full_one_way,
                           'diff_all_same': answer_ant_all_same - answer_full_all_same,
                           'diff_sum': (float(answer_ant_rand - answer_full_rand) / small_diff +
                                        float(answer_ant_one_way - answer_full_one_way) / (local_diff * 2) +
                                        float(answer_ant_all_same - answer_full_all_same) / big_diff)}
                df = df.append(results, ignore_index=True)
                print(results)

    df = df.rename(columns={"diff_all_same": "diff_big", 'diff_rand': 'diff_small', 'diff_one_way': 'diff_local'})
    df = df.sort_values(['diff_sum', 'tmax'], ascending=True)
    df.to_excel(path + f'df_by_sum{file_i}.xlsx')

    # df = df.sort_values(['alpha', ], ascending=True)
    # df.to_excel(path + 'df_by_alpha.xlsx')
    #
    # df = df.sort_values(['po', ], ascending=True)
    # df.to_excel(path + 'df_by_po.xlsx')
    #
    # df = df.sort_values(['tmax', ], ascending=True)
    # df.to_excel(path + 'df_by_tmax.xlsx')

    return df


if __name__ == '__main__':
    print()
    df = make_table()
    #df.show()

