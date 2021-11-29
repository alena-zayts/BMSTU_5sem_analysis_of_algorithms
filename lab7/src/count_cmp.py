import matplotlib.pyplot as plt
from statistics import mean, median
path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab7/report/inc/img/'
count_file = path + 'counts.txt'

DICT_FILENAME = 'ENRUS.TXT'
N = 1000


def load_data(n=N):
    my_dict = dict()

    f = open(DICT_FILENAME, 'r')
    lines = f.readlines()
    f.close()

    done = 0
    for i in range(len(lines) // 2):
        en = lines[i * 2][:-1]
        if len(en.split()) > 1:
            en = en.split()[-1]

        rus = lines[i * 2 + 1][:-1]
        if len(rus.split()) > 1:
            rus = rus.split()[1]

        if en in my_dict.keys():
            # print(f'Ключ "{en}" уже есть в словаре')
            continue

        my_dict[en.lower()] = rus.lower()
        done += 1
        if done == n:
            break

    print(f'Loaded {done} items')
    return my_dict


def sort_by_keys(my_dict, reverse=False):
    sorted_keys = list(my_dict.keys())
    sorted_keys.sort(reverse=reverse)

    return {k: my_dict[k] for k in sorted_keys}


def sort_by_values(my_dict, reverse=False):
    sorted_dict = list(my_dict.items())
    sorted_dict.sort(key=lambda i: i[1], reverse=reverse)

    return {elem[0]: elem[1] for elem in sorted_dict}


def full_search(my_dict, key):
    count = 0
    for cur_key in my_dict.keys():
        count += 1
        if cur_key == key:
            break
    return count, 0


def binary_search(my_dict, key):
    count_k = 0
    count_g = 0
    my_keys = list(my_dict.keys())
    my_len = len(my_keys)
    l = 0
    r = my_len - 1

    while l <= r:
        count_g += 1
        middle = (r + l) // 2
        cur_key = my_keys[middle]

        if cur_key == key:
            count_k += 1
            return count_k, count_g
        elif cur_key > key:
            r = middle - 1
        else:
            l = middle + 1
        count_k += 2

    count_g += 1

    return count_k, count_g




def segmentate(my_dict):
    # создаем словарь частотности сегментов
    seg_frequency_dict = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    for key in my_dict.keys():
        seg_frequency_dict[key[0]] += 1

    # Сортируем по убыванию частотности
    seg_frequency_dict = sort_by_values(seg_frequency_dict, reverse=True)

    # создаем отсортированный словарь сегментов с отсортированными сегментами
    new_dict = {letter: dict() for letter in seg_frequency_dict.keys()}
    for key in my_dict.keys():
        new_dict[key[0]].update({key: my_dict[key]})
    for key in new_dict:
        new_dict[key] = sort_by_keys(new_dict[key])

    return new_dict


def segment_search(my_dict, key):
    count_k = 0
    count_g = 0
    for k in my_dict:
        count_k += 1
        if key[0] == k:
            if my_dict[k]:
                count_kb, count_gb = binary_search(my_dict[k], key)
                count_k += count_kb
                count_g += count_gb
                return count_k, count_g
            else:
                count_k += 1
                return count_k, count_g
    return count_k, count_g


def find_all_keys(my_dict, alg, keys, name):
    results_k = []
    results_g = []
    for key in keys:
        count_k, count_g = alg(my_dict, key)
        results_k.append(count_k)
        results_g.append(count_g)

    with open(path + f'{name}.txt', 'w') as f:
        f.write(' '.join(list(map(str, keys))) + '\n')
        f.write(' '.join(list(map(str, results_k))) + '\n')
        f.write(' '.join(list(map(str, results_g))) + '\n')
    return results_k, results_g


def draw_plots_for_alg(name):
    with open(path + f'{name}.txt', 'r') as f:
        keys = list(map(str, f.readline().split()))
        results_k = list(map(int, f.readline().split()))
        results_g = list(map(int, f.readline().split()))

    for i in range(len(results_g)):
        results_g[i] += results_k[i]

    plt.ylabel('Количество сравнений')
    plt.subplots_adjust(bottom=0.3)
    #plt.grid()
    plt.bar(keys, results_k, width=0.01, color='#0504aa', alpha=0.7)
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_xticklabels([])
    plt.savefig(path + f'{name}_k.png')
    plt.gcf().clear()

    x = zip(keys, results_k)
    xs = sorted(x, key=lambda tup: tup[1], reverse=True)
    keys = [x[0] for x in xs]
    results_k = [x[1] for x in xs]

    plt.ylabel('Количество сравнений')
    #plt.grid()
    plt.bar(keys, results_k, width=0.1, color='#0504aa', alpha=0.7)
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_xticklabels([])
    plt.savefig(path + f'{name}_kg.png')
    plt.gcf().clear()

    print(name)
    print(f'min: {min(results_k)}')
    print(f'max: {max(results_k)}')
    print(f'mean: {mean(results_k)}')
    print(f'median: {median(results_k)}')


def main():
    enrus_dict = load_data()
    enrus_dict = sort_by_keys(enrus_dict)

    find_all_keys(enrus_dict, full_search, enrus_dict.keys(), 'full2')
    draw_plots_for_alg('full2')


    find_all_keys(enrus_dict, binary_search, enrus_dict.keys(), 'binary2')
    draw_plots_for_alg('binary2')



    segmentated_enrus_dict = segmentate(enrus_dict)
    find_all_keys(segmentated_enrus_dict, segment_search, enrus_dict.keys(), 'segment2')
    draw_plots_for_alg('segment2')



if __name__ == "__main__":
    main()