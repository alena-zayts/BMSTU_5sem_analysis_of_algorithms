from my_dict import *
from time import process_time
import matplotlib.pyplot as plt

path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab7/report/inc/img/'
time_file = path + 'times.txt'
filename_all = path + 'time_all.png'
n_repeats = [3,]
ns = [100, 1000, 5000, 10000, 40000]


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
    efss = []
    nfss = []
    ebss = []
    nbss = []
    esss = []
    nsss = []
    for n in ns:
        enrus_dict = load_data(n)
        keys = enrus_dict.keys()

        efs, nfs = count_time_for_alg(enrus_dict, full_search, keys)

        sorted_enrus_dict = sort_by_keys(enrus_dict)
        ebs, nbs = count_time_for_alg(sorted_enrus_dict, binary_search, keys)

        segmentated_enrus_dict = segmentate(enrus_dict)
        ess, nss = count_time_for_alg(segmentated_enrus_dict, segment_search, keys)

        if len(efs + nfs + ebs + nbs + ess + nss) > 6:
            print('dfhbnvo;spguehrpufghor')
        efss.append(efs[0]/n_repeats[0])
        nfss.append(nfs[0]/n_repeats[0])
        ebss.append(ebs[0]/n_repeats[0])
        nbss.append(nbs[0]/n_repeats[0])
        esss.append(ess[0]/n_repeats[0])
        nsss.append(efs[0]/n_repeats[0])

    with open(time_file, 'w') as f:
        f.write(' '.join(list(map(str, ns))) + '\n')
        f.write(' '.join(list(map(str, efss))) + '\n')
        f.write(' '.join(list(map(str, nfss))) + '\n')
        f.write(' '.join(list(map(str, ebss))) + '\n')
        f.write(' '.join(list(map(str, nbss))) + '\n')
        f.write(' '.join(list(map(str, esss))) + '\n')
        f.write(' '.join(list(map(str, nsss))) + '\n')


def draw_plot_all():
    with open(time_file, 'r') as f:
        ns = list(map(float, f.readline().split()))
        efs = list(map(float, f.readline().split()))
        nfs = list(map(float, f.readline().split()))
        ebs = list(map(float, f.readline().split()))
        nbs = list(map(float, f.readline().split()))
        ess = list(map(float, f.readline().split()))
        nss = list(map(float, f.readline().split()))

    plt.xlabel('Количество элементов в словаре')
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
    # cmp_time()
    draw_plot_all()


