from my_dict import *
from time import process_time
import matplotlib.pyplot as plt

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab7/report/inc/img/'
time_file = path + 'times.txt'
filename_all = path + 'time_all.png'
n_repeats = [1, 10**2, 10**3, 10**4, 10**5, 10**8]


def find_all_keys(my_dict, alg, exist, keys):
    for key in keys:
        if not exist:
            key += '&'
        value = alg(my_dict, key)
        if exist != (str(value) != '-1'):
            print('err')


def count_time_for_alg(my_dict, alg, keys):
    exist_list = []
    not_exist_list = []
    for n in n_repeats:
        print(n)
        start = process_time()
        for _ in range(n):
            find_all_keys(my_dict, alg, True, keys)
        end = process_time()
        exist_list.append(end-start)

        start = process_time()
        for _ in range(n):
            find_all_keys(my_dict, alg, False, keys)
        end = process_time()
        not_exist_list.append(end-start)

    return exist_list, not_exist_list


def cmp_time():
    enrus_dict = load_data()
    keys = enrus_dict.keys()

    efs, nfs = count_time_for_alg(enrus_dict, full_search, keys)

    sorted_enrus_dict = sort_by_keys(enrus_dict)
    ebs, nbs = count_time_for_alg(sorted_enrus_dict, binary_search, keys)

    segmentated_enrus_dict = segmentate(enrus_dict)
    ess, nss = count_time_for_alg(segmentated_enrus_dict, segment_search, keys)

    with open(time_file, 'w') as f:
        f.write(' '.join(list(map(str, n_repeats))) + '\n')
        f.write(' '.join(list(map(str, efs))) + '\n')
        f.write(' '.join(list(map(str, nfs))) + '\n')
        f.write(' '.join(list(map(str, ebs))) + '\n')
        f.write(' '.join(list(map(str, nbs))) + '\n')
        f.write(' '.join(list(map(str, ess))) + '\n')
        f.write(' '.join(list(map(str, nss))) + '\n')


def draw_plot_all():
    with open(time_file, 'r') as f:
        ns = list(map(float, f.readline().split()))
        efs = list(map(float, f.readline().split()))
        nfs = list(map(float, f.readline().split()))
        ebs = list(map(float, f.readline().split()))
        nbs = list(map(float, f.readline().split()))
        ess = list(map(float, f.readline().split()))
        nss = list(map(float, f.readline().split()))

    plt.xlabel('Количество проходов')
    plt.xticks(ns)
    # plt.figure(figsize=(7, 10))
    plt.ylabel('Время работы реализации (с)')
    plt.grid()

    plt.plot(ns, efs, label='full_e', linestyle='-.', color='green')
    plt.plot(ns, nfs, label='full_n', color='green')

    plt.plot(ns, ebs, label='binary_e', linestyle='-.', color='blue')
    plt.plot(ns, nbs, label='binary_n', color='blue')

    plt.plot(ns, ess, label='segment_e', linestyle='-.', color='red')
    plt.plot(ns, nss, label='segment_n', color='red')

    plt.legend(loc='best')
    plt.savefig(filename_all)


if __name__ == "__main__":
    cmp_time()
    draw_plot_all()


