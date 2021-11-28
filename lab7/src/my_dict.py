
DICT_FILENAME = 'ENRUS.TXT'
N = 30
DEBUG = False


def load_data():
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
        if done == N:
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
    for cur_key in my_dict.keys():
        if cur_key == key:
            return my_dict[cur_key]
    return -1


# def binary_search(my_dict, key):
#     my_keys = list(my_dict.keys())
#     my_len = len(my_keys)
#     l = 0
#     r = my_len
#
#     while l <= r:
#         middle = (r + l) // 2
#         cur_key = my_keys[middle]
#
#         if cur_key == key:
#             return my_dict[cur_key]
#         elif cur_key > key:
#             r = middle - 1
#         else:
#             l = middle + 1
#
#     return -1

def binary_search(my_dict, key):
    my_keys = list(my_dict.keys())
    my_len = len(my_keys)

    low = 0
    high = my_len - 1
    mid = my_len // 2

    while my_keys[mid] != key and low <= high:
        if key > my_keys[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1

    return my_dict[my_keys[mid]]


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
    for k in my_dict:
        if key[0] == k:
            if my_dict[k]:
                return binary_search(my_dict[k], key)
            else:
                return -1
    return -1


def main():
    enrus_dict = load_data()
    if DEBUG:
        print(enrus_dict)


    key = input("Input key: ")
    print(f'Python search: {enrus_dict.get(key)}')


    value = full_search(enrus_dict, key)
    print(f"Full search: {value}")



    sorted_enrus_dict = sort_by_keys(enrus_dict)
    if DEBUG:
        print('sorted')
        print(sorted_enrus_dict)
    value = binary_search(sorted_enrus_dict, key)
    print(f"Binary search: {value}")


    segmentated_enrus_dict = segmentate(enrus_dict)
    if DEBUG:
        print('segmentated')
        print(segmentated_enrus_dict)
    value = segment_search(segmentated_enrus_dict, key)
    print(f"Segment search: {value}")




if __name__ == "__main__":
    main()