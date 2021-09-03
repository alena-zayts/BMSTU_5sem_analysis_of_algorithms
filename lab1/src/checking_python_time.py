from algorythms import *

n = 100000
str1 = 'кот1234567'
str2 = 'скат1234'

def main_function1():
    beg = time.time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.time()
    print(f'time:{end - beg}')

    beg = time.thread_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.thread_time()
    print(f'thread_time:{end - beg}')

    beg = time.process_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.process_time()
    print(f'process_time():{end - beg}')


def main_function2():
    beg = time.thread_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.thread_time()
    print(f'thread_time:{end - beg}')

    beg = time.process_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.process_time()
    print(f'process_time():{end - beg}')

    beg = time.time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.time()
    print(f'time:{end - beg}')


def main_function3():
    beg = time.process_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.process_time()
    print(f'process_time():{end - beg}')

    beg = time.time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.time()
    print(f'time:{end - beg}')

    beg = time.thread_time()
    for i in range(n):
        lowenstein_dist_matrix_classic(str1, str2)
    end = time.thread_time()
    print(f'thread_time:{end - beg}')


if __name__ == '__main__':
    main_function1()
    print()
    main_function2()
    print()
    main_function3()
