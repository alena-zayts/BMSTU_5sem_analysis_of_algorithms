import string
import random
from algorythms import *


def random_string(lenght):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(lenght))


class TestDistance:
    def __init__(self, function, func_name, xchange):
        self.function = function
        self.func_name = func_name
        self.xchange = xchange

    def test_empty(self):
        print(f'testing empty for {self.func_name}')
        assert self.function("", "") == 0
        print('OK\n')

    def test_equal(self):
        print(f'testing equal for {self.func_name}')
        assert self.function("abc", "abc") == 0
        assert self.function("a", "a") == 0
        print('OK\n')

    def test_different(self):
        print(f'testing different for {self.func_name}')
        assert self.function("a", "") == 1
        assert self.function("", "a") == 1
        assert self.function("b", "c") == 1
        assert self.function("bc", "b") == 1
        assert self.function("bc", "c") == 1
        assert self.function("bc", "ac") == 1
        assert self.function("ab", "cd") == 2
        assert self.function("abc", "cd") == 3
        assert self.function("кот", "скат") == 2
        print('OK\n')

    def test_xchange(self):
        print(f'testing xchange for {self.func_name}')
        if not self.xchange:
            assert self.function("ac", "ca") == 2
            assert self.function("qac", "lca") == 3
            assert self.function("abc", "cba") == 2
        else:
            assert self.function("ac", "ca") == 1
            assert self.function("qac", "lca") == 2
            assert self.function("abc", "cba") == 2

        print('OK\n')

    def run_tests(self):
        self.test_empty()
        self.test_equal()
        self.test_different()
        self.test_xchange()


class TestTwoFunctions:
    n = 7
    lenght = 10
    dif = 2

    def __init__(self, f1, f1_name, f2, f2_name):
        self.f1 = f1
        self.f1_name = f1_name
        self.f2 = f2
        self.f2_name = f2_name

    def test_same_len(self):
        print(f'testing same_len for {self.f1_name} and {self.f2_name}')
        for i in range(self.n):
            str1 = random_string(self.lenght)
            str2 = random_string(self.lenght)
            print(f'with str1={str1} and str2={str2}')
            assert self.f1(str1, str2) == self.f2(str1, str2)

    def test_different_len(self):
        print(f'testing different_len for {self.f1_name} and {self.f2_name}')
        for i in range(TestTwoFunctions.n):
            str1 = random_string(self.lenght + self.dif)
            str2 = random_string(self.lenght - self.dif)
            print(f'with str1={str1} and str2={str2}')
            assert self.f1(str1, str2) == self.f2(str1, str2)
            print(f'with str1={str2} and str2={str1}')
            assert self.f1(str2, str1) == self.f2(str2, str1)

    def run_tests(self):
        self.test_same_len()
        self.test_different_len()


if __name__ == '__main__':
    test = TestDistance(lowenstein_dist_matrix_classic, 'lowenstein_dist_matrix_classic', False)
    test.run_tests()
    test = TestDistance(lowenstein_dist_matrix_optimized, 'lowenstein_dist_matrix_optimized', False)
    test.run_tests()
    test = TestDistance(lowenstein_dist_recursion_classic, 'lowenstein_dist_recursion_classic', False)
    test.run_tests()
    test = TestDistance(lowenstein_dist_recursion_optimized, 'lowenstein_dist_recursion_optimized', False)
    test.run_tests()
    test = TestDistance(damerau_lowenstein_dist_recursion, 'damerau_lowenstein_dist_recursion', True)
    test.run_tests()

    ###
    test = TestTwoFunctions(lowenstein_dist_matrix_classic, 'lowenstein_dist_matrix_classic',
                            lowenstein_dist_matrix_optimized, 'lowenstein_dist_matrix_optimized')
    test.run_tests()
    test = TestTwoFunctions(lowenstein_dist_matrix_classic, 'lowenstein_dist_matrix_classic',
                            lowenstein_dist_recursion_classic, 'lowenstein_dist_recursion_classic')
    test.run_tests()
    test = TestTwoFunctions(lowenstein_dist_matrix_classic, 'lowenstein_dist_matrix_classic',
                            lowenstein_dist_recursion_optimized, 'lowenstein_dist_recursion_optimized')
    test.run_tests()

    ###
    test = TestTwoFunctions(lowenstein_dist_matrix_optimized, 'lowenstein_dist_matrix_optimized',
                            lowenstein_dist_recursion_classic, 'lowenstein_dist_recursion_classic')
    test.run_tests()

    test = TestTwoFunctions(lowenstein_dist_matrix_optimized, 'lowenstein_dist_matrix_optimized',
                            lowenstein_dist_recursion_optimized, 'lowenstein_dist_recursion_optimized')
    test.run_tests()

    ##
    test = TestTwoFunctions(lowenstein_dist_recursion_classic, 'lowenstein_dist_recursion_classic',
                            lowenstein_dist_recursion_optimized, 'lowenstein_dist_recursion_optimized')
    test.run_tests()
