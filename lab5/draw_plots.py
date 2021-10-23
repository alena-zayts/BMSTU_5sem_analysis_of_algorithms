import matplotlib.pyplot as plt


path = 'C:/Users/alena/Desktop/BMSTU_5sem_analysis_of_algorithms/lab5/report/inc/img/'
time_file = 'C:/msys64/home/alena/build-lab5-Desktop_Qt_MinGW_w64_64bit_MSYS2-Debug/times.txt'
filename_all = path + 'time_all.png'


def draw_plot_all():
    n_tasks = []
    times_lin = []
    times_paral = []

    with open(time_file, 'r') as f:
        for stats in f.readlines():
            print(stats)
            stats = stats.split()
            n_tasks.append(int(stats[0]))
            times_lin.append(float(stats[1])/1000)
            times_paral.append(float(stats[2])/1000)

    plt.xlabel('Количество задач')
    plt.xticks(n_tasks)
    plt.ylabel('Время работы реализации (c)')
    plt.grid()

    plt.plot(n_tasks, times_lin, label='Последовательная')
    plt.plot(n_tasks, times_paral, label='Параллельная')

    plt.legend(loc='best')
    plt.savefig(filename_all)


if __name__ == '__main__':
    draw_plot_all()
