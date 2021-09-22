from copy import deepcopy
from time import process_time
import matplotlib.pyplot as plt
from algorythms import *
from random import randint
import pandas as pd

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab2/report/inc/img/'
time_file = path + 'time_w.xlsx'
filename_all = path + 'time_all_w.png'


def time_compare():
    standart = []
    vinograd = []
    vinograd_optimized = []

    n_list = list(range(101, 1002, 100))

    for i in range(len(n_list)):
        n = n_list[i]
        n_repeats = max(5 - i, 1)
        print(f'\nn: {n}, n_repeats: {n_repeats}')

        a = [[randint(0, 10) for i in range(n)] for i in range(n)]
        b = [[randint(0, 10) for i in range(n)] for i in range(n)]
        c = [[0 for i in range(n)] for i in range(n)]

        print('Стандартный алгоритм')
        time = 0
        for j in range(n_repeats):
            start = process_time()
            answer = standart_mult(a, b, c, n, n, n)
            end = process_time()
            time += (end - start)
        time /= n_repeats
        print('time:', time)
        standart.append(time)


        print('Алгоритм Винограда')
        time = 0
        for j in range(n_repeats):
            start = process_time()
            answer = vinograd_usual_mult(a, b, c, n, n, n)
            end = process_time()
            time += (end - start)
        time /= n_repeats
        print('time:', time)
        vinograd.append(time)

        print('Оптимизированный алгоритм Винограда')
        time = 0
        for j in range(n_repeats):
            start = process_time()
            answer = vinograd_optimized_mult(a, b, c, n, n, n)
            end = process_time()
            time += (end - start)
        time /= n_repeats
        print('time:', time)
        vinograd_optimized.append(time)

    df = pd.DataFrame({'N': n_list})
    df['standart'] = standart
    df['vinograd'] = vinograd
    df['vinograd_optimized'] = vinograd_optimized

    df.to_excel(time_file)


def draw_plot_all():
    df = pd.read_excel(time_file)

    plt.xlabel('Размерность матриц (n*n)')
    plt.ylabel('Время работы реализации (c)')
    plt.grid()

    plt.plot(df['N'], df['standart'], label='Стандартный')
    plt.plot(df['N'], df['vinograd'], label='Винограда')
    plt.plot(df['N'], df['vinograd_optimized'], label='Винограда, опт.')

    plt.legend(loc='best')
    plt.savefig(filename_all)
    plt.gcf().clear()


if __name__ == '__main__':
    time_compare()
    draw_plot_all()
