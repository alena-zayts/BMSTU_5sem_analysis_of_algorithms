import matplotlib.pyplot as plt


path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab4/report/inc/img/'
time_file = path + 'time.txt'
filename_all = path + 'time_all.png'


def draw_plot_all():
    n_objects = [5, 10, 15, 20, 25, 30, 35]
    n_threads = [1, 2, 4, 8, 16, 32]

    times_basic = []
    times_threads = [[] for i in range(len(n_threads))]
    with open(time_file, 'r') as f: #, encoding="utf-8"
        for i in range(len(n_objects)):
            measures = f.readline().split()
            times_basic.append(float(measures[0][6:-1].replace(',', '.')))
            for i in range(len(n_threads)):
                times_threads[i].append(float(measures[i + 1].replace(',', '.')))

    times_basic = [3.2853632875, 6.2137912125, 9.1487571625, 13.4555683, 15.134954425, 20.138483425, 22.27747595]
    plt.xlabel('Количество объектов на сцене')
    plt.xticks(n_objects)
    plt.ylabel('Время работы реализации (c)')
    plt.grid()

    plt.plot(n_objects, times_basic, label='Последовательный')
    print(times_basic)
    for i in range(len(n_threads)):
        plt.plot(n_objects, times_threads[i], label=f'Параллельный, n_threads={n_threads[i]}')
        print(times_threads[i])

    plt.legend(loc='best')
    plt.savefig(filename_all)
    plt.gcf().clear()


if __name__ == '__main__':
    draw_plot_all()
