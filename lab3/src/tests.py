from algorythms import *
from copy import deepcopy


tests_dict = {
    'empty': [],
    'one_elem': [1],
    'sorted_10': list(range(10)),
    'sorted_back_10': list(range(9, -1, -1)),
    'random': [random.randint(0, 10) for i in range(10)]
}


def test_alg(func, alg_name):
    print(f'\n\nТестируемый алгоритм: {alg_name}')
    for test_name, test_arr in tests_dict.items():
        print(test_name)
        print('До сортировки:', test_arr)
        answer = func(deepcopy(test_arr), len(test_arr))
        print('После сортировки:', answer)
        print()


def test_all():
    test_alg(insertion_sort, 'Сортировка вставками')
    test_alg(bubble_sort, 'Пузырьковая сортировка')
    test_alg(shaker_sort, 'Шейкерная сортировка')

if __name__ == '__main__':
    test_all()