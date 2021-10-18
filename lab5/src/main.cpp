#include <iostream>
#include <thread>

#include "conveyor.h"
#define N 100000

int main()
{
    double a[N];
    for (int i = 0; i <N; i++)
        a[i] = i;

    double b[N];

    int n_tasks;
    std::cout << "Number of tasks: ";
    std::cin >> n_tasks;

    setbuf(stdout, NULL);
    Conveyor *conveyor_obj = new Conveyor();

    //
    system_clock::time_point begin = system_clock::now();
    system_clock::duration tp_begin = begin.time_since_epoch();
    tp_begin -= duration_cast<seconds>(tp_begin);
    time_t tt_begin = system_clock::to_time_t(begin);
    tm t_begin = *gmtime(&tt_begin);

    conveyor_obj->run_parallel(n_tasks, N, a, b);

    system_clock::time_point end = system_clock::now();
    system_clock::duration tp_end = end.time_since_epoch();
    tp_end -= duration_cast<seconds>(tp_end);
    time_t tt_end = system_clock::to_time_t(end);
    tm t_end = *gmtime(&tt_end);

    int h_dur = t_end.tm_hour - t_begin.tm_hour;
    int m_dur = t_end.tm_min - t_begin.tm_min;
    int s_dur = t_end.tm_sec - t_begin.tm_sec;
    system_clock::duration ms_dur = tp_end - tp_begin;
    //

    conveyor_obj->make_stats(n_tasks);

    //
    system_clock::time_point begin_l = system_clock::now();
    system_clock::duration tp_begin_l = begin_l.time_since_epoch();
    tp_begin_l -= duration_cast<seconds>(tp_begin_l);
    time_t tt_begin_l = system_clock::to_time_t(begin_l);
    tm t_begin_l = *gmtime(&tt_begin_l);

    conveyor_obj->run_linear(n_tasks, N, a, b);

    system_clock::time_point end_l = system_clock::now();
    system_clock::duration tp_end_l = end_l.time_since_epoch();
    tp_end_l -= duration_cast<seconds>(tp_end_l);
    time_t tt_end_l = system_clock::to_time_t(end_l);
    tm t_end_l = *gmtime(&tt_end_l);

    int h_dur_l = t_end_l.tm_hour - t_begin_l.tm_hour;
    int m_dur_l = t_end_l.tm_min - t_begin_l.tm_min;
    int s_dur_l = t_end_l.tm_sec - t_begin_l.tm_sec;
    system_clock::duration ms_dur_l = tp_end_l - tp_begin_l;
    //

    conveyor_obj->make_stats(n_tasks);


    //
    std::printf("Duration parallel %02u:%02u:%02u.%3u\n",
                h_dur, m_dur, s_dur,
                static_cast<unsigned>(ms_dur / milliseconds(1))
    );

    std::printf("Duration linear %02u:%02u:%02u.%3u\n",
                h_dur_l, m_dur_l, s_dur_l,
                static_cast<unsigned>(ms_dur_l / milliseconds(1))
    );

    //

//    for (int i = 0; i < N; i++)
//        std::cout << b[i] << std::endl;



//    system_clock::time_point now = system_clock::now();
//    system_clock::duration tp = now.time_since_epoch();

//    tp -= duration_cast<seconds>(tp);

//    time_t tt = system_clock::to_time_t(now);
//    tm t = *gmtime(&tt);

//    std::printf("Task %4d | %s | %02u:%02u:%02u.%3u\n",
//                task_num,
//                event,
//                t.tm_hour,
//                t.tm_min,
//                t.tm_sec,
//                static_cast<unsigned>(tp / milliseconds(1))
//    );

    delete conveyor_obj;

    return 0;
}
