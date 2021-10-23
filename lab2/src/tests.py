from algorythms import *
from copy import deepcopy


def compare_ms(m1, m2):
    for line1, line2 in zip(m1, m2):
        for elem1, elem2 in zip(line1, line2):
            if elem1 != elem2:
                return False
    return True


tests_dict = {
    'empty': {'a': [[]], 'b': [[]], 'c': [[]], 'm': 0, 'n': 0, 'q': 0, 'answer': [[]]},

    'one': {'a': [[2]], 'b': [[2]], 'c': [[0]], 'm': 1, 'n': 1, 'q': 1, 'answer': [[4]]},

    'usual, n=2': {'a': [[1, 1], [1, -1], [2, 2]],
                   'b': [[0, -1, 1, 2], [0, 1, 1, 3]],
                   'c': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   'm': 3, 'n': 2, 'q': 4,
                   'answer': [[0, 0, 2, 5], [0, -2, 0, -1], [0, 0, 4, 10]]},

    'square, n=3': {'a': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                    'b': [[1, 2, 3], [0, 0, 0], [1, 1, 1]],
                    'c': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    'm': 3, 'n': 3, 'q': 3,
                    'answer': [[2, 3, 4], [2, 3, 4], [2, 3, 4]]},
}


def test_alg(func, alg_name):
    print(f'\n\nТестируемый алгоритм: {alg_name}')
    for test_name, test in tests_dict.items():
        print(test_name)
        print('A:')
        print_matrix(test['a'])
        print('B:')
        print_matrix(test['b'])
        result = func(deepcopy(test['a']), deepcopy(test['b']), deepcopy(test['c']), test['m'], test['n'], test['q'])
        print('Result:')
        print_matrix(result)
        if not compare_ms(result, test['answer']):
            print('ERROR')
            print('expected: ')
            print_matrix(test['answer'])
            raise Exception
        print()


def test_all():
    test_alg(standart_mult, 'Стандартный алгоритм')
    test_alg(vinograd_usual_mult, 'Алгоритм Винограда')
    test_alg(vinograd_optimized_mult, 'Оптимизированный алгоритм Винограда')


if __name__ == '__main__':
    #test_all()
    # y = (x - mean) / standard_deviation
    # mean = sum(x) / count(x)
    # standard_deviation = sqrt(sum((x - mean) ^ 2) / count(x))
    x = [1, 2, 3, 4]
    n = len(x)

    sum = 0
    for i in range(n):
        sum += x[i]
    mean = float(sum) / n

    sum = 0
    for i in range(n):
        sum += (x[i] - mean) ** 2
    std: float = (sum / n) ** (1/2)

    for i in range(n):
        x[i] = (x[i] - mean) / std



    print(x)

    sum = 0
    for i in range(n):
        sum += x[i]
    mean = float(sum) / n
    print(mean)
    sum = 0
    for i in range(n):
        sum += (x[i] - mean) ** 2
    std: float = (sum / n) ** (1/2)

    print(std)