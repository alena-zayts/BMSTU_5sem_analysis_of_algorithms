import random
from copy import deepcopy
import pandas as pd
from time import process_time


def insertion_sort(arr, n):
    for i in range(1, n):
        j = i
        cur = arr[j]
        while arr[j - 1] > cur and j > 0:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur
    return arr


# best - sorted
# worst - sorted back
def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def shaker_sort(arr, n):
    left = 0
    right = n - 1
    while left <= right:
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1
        for i in range(left, right, 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
        right -= 1

    return arr


def answer_user():
    #arr = list(map(int, input('Введите массив (в одну строку):\n ').split()))
    arr = list(range(5000, 0, -1))

    print(f'\nПузырьковая сортировка:')
    print('До:')
    print(*arr)
    beg = process_time()
    answer = bubble_sort(deepcopy(arr), len(arr))
    end = process_time()
    print('Ответ:')
    print(*answer)
    print(f'Время: {end-beg}')

    print(f'\nШейкерная сортировка:')
    print('До:')
    print(*arr)
    beg = process_time()
    answer = shaker_sort(deepcopy(arr), len(arr))
    end = process_time()
    print('Ответ:')
    print(*answer)
    print(f'Время: {end-beg}')

    print(f'\nСортировка вставками:')
    print('До:')
    print(*arr)
    beg = process_time()
    answer = insertion_sort(deepcopy(arr), len(arr))
    end = process_time()
    print('Ответ:')
    print(*answer)
    print(f'Время: {end-beg}')

    print()
    print()


if __name__ == '__main__':
    while True:
        answer_user()
















if __name__ == '__main__':
    # print('SHAKER')
    # for test_arr in tests_dict.values():
    #     print(f'Before: {test_arr}')
    #     answer = shaker_sort(test_arr)
    #     print(f'After:  {answer}')
    #     print()

    # print('MERGE')
    # for test_arr in tests_dict.values():
    #     print(f'Before: {test_arr}')
    #     answer = merge_sort(test_arr)
    #     print(f'After:  {answer}')
    #     print()

    a = list(range(10000))
    print(a)
    insertion_sort(a, 10000)
    print(a)