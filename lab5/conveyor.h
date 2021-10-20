#ifndef __CONVEYOR_H__
#define __CONVEYOR_H__

#include <thread>
#include <queue>

#include "slau_solver.h"

#define THRD_CNT 3

class Conveyor
{
public:
    Conveyor() = default;
    ~Conveyor() = default;

    void run_parallel(size_t cars_cnt);
    void run_linear(size_t cars_cnt);

    void create_engine();
    void create_carcass();
    void create_wheels();

private:
    std::thread threads[THRD_CNT];
    std::vector<std::shared_ptr<SlauSolver>> cars;

    std::queue<std::shared_ptr<SlauSolver>> q1;
    std::queue<std::shared_ptr<SlauSolver>> q2;
    std::queue<std::shared_ptr<SlauSolver>> q3;
};

#endif
