#ifndef __CONVEYOR_H__
#define __CONVEYOR_H__

#include <thread>
#include <queue>

#include "standardizer.h"

#define THRD_CNT 3

class Conveyor
{
public:
    Conveyor() = default;
    ~Conveyor() = default;

    void run_parallel(size_t n_tasks, int n, double *arr, double *new_arr);
    void run_linear(size_t n_tasks, int n, double *arr, double *new_arr);

    void find_mean();
    void find_std_dev();
    void transform();

    void make_stats(size_t n_tasks);
    int time_dif(system_clock::time_point begin, system_clock::time_point end, char t);

    std::vector<std::shared_ptr<Standardizer>> tasks;

private:
    std::thread threads[THRD_CNT];

    std::queue<std::shared_ptr<Standardizer>> q1;
    std::queue<std::shared_ptr<Standardizer>> q2;
    std::queue<std::shared_ptr<Standardizer>> q3;
};

#endif
