from algs import *
from time_cmp import generate_matrix_all_same, generate_matrix_random, generate_matrix_one_way
from tests import print_matrix
from copy import copy
import pandas as pd

alphas = [0.1, 0.25, 0.5, 0.75, 0.9]
pos = copy(alphas)
tmaxs = [100, 200, 300, 400, 500]

# alphas = alphas[:3]
# pos = pos[:3]
# tmaxs = tmaxs[:3]

n_cities = 11

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab6/report/inc/img/'
df_file = path + 'df.xlsx'


def make_table():
    df = pd.DataFrame(columns=['alpha', 'po', 'tmax', 'diff_rand', 'diff_one_way', 'diff_all_same'])

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
                           'diff_one_way': answer_ant_one_way-answer_full_one_way,
                           'diff_all_same': answer_ant_all_same-answer_full_all_same}
                df = df.append(results, ignore_index=True)
                print(results)

    df = df.rename(columns={"diff_all_same": "diff_rand_2"})
    df = df.sort_values(['diff_rand_2', 'diff_rand', 'diff_one_way'], ascending=False)
    df.to_excel(df_file)
    return df


if __name__ == '__main__':
    print()
    # df = make_table()
    #df.show()

