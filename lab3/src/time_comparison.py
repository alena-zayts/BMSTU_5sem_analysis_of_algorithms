from copy import deepcopy
from time import process_time
import matplotlib.pyplot as plt
from algorythms import *

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab3/report/inc/img/'

time_file = path + 'time.xlsx'

filename_all = path + 'time_all.png'

filename_insertion = path + 'time_insertion.png'
filename_bubble = path + 'time_bubble.png'
filename_shaker = path + 'time_shaker.png'

filename_best = path + 'time_best.png'
filename_worst = path + 'time_worst.png'
filename_middle = path + 'time_middle.png'


def time_compare():

    def count_middle_time(n, arr, alg, n_repeats):
        time = 0
        for i in range(n_repeats):
            current = deepcopy(arr)
            start = process_time()
            answer = alg(current, n)
            end = process_time()
            time += (end - start)
        time /= n_repeats
        return time

    n_repeats = 5
    n_list = list(range(0, 100, 10)) + list(range(100, 500, 100)) + \
             list(range(500, 2000, 500)) + list(range(2000, 5001, 1000))

    insertion_dict = {'best': [], 'worst': [], 'middle': []}
    bubble_dict = {'best': [], 'worst': [], 'middle': []}
    shaker_dict = {'best': [], 'worst': [], 'middle': []}

    for n in n_list:
        print(n)
        print('best')
        best = list(range(0, n, 1))
        insertion_dict['best'].append(count_middle_time(n, best, insertion_sort, n_repeats))
        bubble_dict['best'].append(count_middle_time(n, best, bubble_sort, n_repeats))
        shaker_dict['best'].append(count_middle_time(n, best, shaker_sort, n_repeats))

        print('worst')
        worst = list(range(n, 0, -1))
        insertion_dict['worst'].append(count_middle_time(n, worst, insertion_sort, n_repeats))
        bubble_dict['worst'].append(count_middle_time(n, worst, bubble_sort, n_repeats))
        shaker_dict['worst'].append(count_middle_time(n, worst, shaker_sort, n_repeats))

        print('middle')
        middle = [random.randint(0, n) for i in range(n)]
        insertion_dict['middle'].append(count_middle_time(n, middle, insertion_sort, n_repeats))
        bubble_dict['middle'].append(count_middle_time(n, middle, bubble_sort, n_repeats))
        shaker_dict['middle'].append(count_middle_time(n, middle, shaker_sort, n_repeats))

    df = pd.DataFrame({'N': n_list})
    df['insertion_best'] = insertion_dict['best']
    df['insertion_worst'] = insertion_dict['worst']
    df['insertion_middle'] = insertion_dict['middle']

    df['bubble_best'] = bubble_dict['best']
    df['bubble_worst'] = bubble_dict['worst']
    df['bubble_middle'] = bubble_dict['middle']

    df['shaker_best'] = shaker_dict['best']
    df['shaker_worst'] = shaker_dict['worst']
    df['shaker_middle'] = shaker_dict['middle']

    df.to_excel(time_file)


def draw_plot_all():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')
    plt.grid()

    plt.plot(df['N'], df['insertion_best'], label='insertion_best')
    plt.plot(df['N'], df['bubble_best'], label='bubble_best')
    plt.plot(df['N'], df['shaker_best'], label='shaker_best')

    plt.plot(df['N'], df['insertion_worst'], label='insertion_worst')
    plt.plot(df['N'], df['bubble_worst'], label='bubble_worst')
    plt.plot(df['N'], df['shaker_worst'], label='shaker_worst')

    plt.plot(df['N'], df['insertion_middle'], label='insertion_middle')
    plt.plot(df['N'], df['bubble_middle'], label='bubble_middle')
    plt.plot(df['N'], df['shaker_middle'], label='shaker_middle')

    plt.legend(loc='best')
    plt.savefig(filename_all)
    plt.gcf().clear()


def draw_plot_insertion():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['insertion_best'], label='insertion_best')
    plt.plot(df['N'], df['insertion_worst'], label='insertion_worst')
    plt.plot(df['N'], df['insertion_middle'], label='insertion_middle')

    plt.legend(loc='best')
    plt.savefig(filename_insertion)
    plt.gcf().clear()


def draw_plot_bubble():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['bubble_best'], label='bubble_best')
    plt.plot(df['N'], df['bubble_worst'], label='bubble_worst')
    plt.plot(df['N'], df['bubble_middle'], label='bubble_middle')

    plt.legend(loc='best')
    plt.savefig(filename_bubble)
    plt.gcf().clear()


def draw_plot_shaker():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['shaker_best'], label='shaker_best')
    plt.plot(df['N'], df['shaker_worst'], label='shaker_worst')
    plt.plot(df['N'], df['shaker_middle'], label='shaker_middle')

    plt.legend(loc='best')
    plt.savefig(filename_shaker)
    plt.gcf().clear()


def draw_plot_best():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['insertion_best'], label='insertion_best')
    plt.plot(df['N'], df['bubble_best'], label='bubble_best')
    plt.plot(df['N'], df['shaker_best'], label='shaker_best')

    plt.legend(loc='best')
    plt.savefig(filename_best)
    plt.gcf().clear()


def draw_plot_worst():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['insertion_worst'], label='insertion_worst')
    plt.plot(df['N'], df['bubble_worst'], label='bubble_worst')
    plt.plot(df['N'], df['shaker_worst'], label='shaker_worst')

    plt.legend(loc='best')
    plt.savefig(filename_worst)
    plt.gcf().clear()


def draw_plot_middle():
    df = pd.read_excel(time_file)

    plt.xlabel('Длина массива')
    plt.ylabel('Время работы реализации (c)')

    plt.plot(df['N'], df['insertion_middle'], label='insertion_middle')
    plt.plot(df['N'], df['bubble_middle'], label='bubble_middle')
    plt.plot(df['N'], df['shaker_middle'], label='shaker_middle')

    plt.legend(loc='best')
    plt.savefig(filename_middle)
    plt.gcf().clear()


def draw_plots():
    draw_plot_all()

    draw_plot_bubble()
    draw_plot_insertion()
    draw_plot_shaker()

    draw_plot_best()
    draw_plot_worst()
    draw_plot_middle()


if __name__ == '__main__':
    # time_compare()
    draw_plots()
