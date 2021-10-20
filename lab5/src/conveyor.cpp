#include "conveyor.h"

void Conveyor::run_parallel(size_t n_tasks, int n, double *arr, double *new_arr)
{
    for (size_t i = 0; i < n_tasks; i++)
    {
        std::shared_ptr<Standardizer> new_task(new Standardizer(n, arr, new_arr));
        q1.push(new_task);
        new_task->in1 = system_clock::now();
    }

    this->threads[0] = std::thread(&Conveyor::find_mean, this, n_tasks);
    this->threads[1] = std::thread(&Conveyor::find_std_dev, this);
    this->threads[2] = std::thread(&Conveyor::transform, this);

    for (int i = 0; i < THRD_CNT; i++)
    {
        if (this->threads[i].joinable())
            this->threads[i].join();
    }
}

void Conveyor::run_linear(size_t n_tasks, int n, double *arr, double *new_arr)
{
    for (size_t i = 0; i < n_tasks; i++)
    {
        std::shared_ptr<Standardizer> new_task(new Standardizer(n, arr, new_arr));

        q1.push(new_task);
        new_task->in1 = system_clock::now();
    }

    for (size_t i = 0; i < n_tasks; i++)
    {
        std::shared_ptr<Standardizer> task = q1.front();
        task->out1 = system_clock::now();
        task->find_mean(i + 1);
        q2.push(task);
        task->in2 = system_clock::now();
        q1.pop();

        task = q2.front();
        task->out2 = system_clock::now();
        task->find_std_dev(i + 1);
        q3.push(task);
        task->in3 = system_clock::now();
        q2.pop();

        task = q3.front();
        task->out3 =system_clock::now();
        task->transform(i + 1);
        tasks.push_back(task);
        task->out_system = system_clock::now();
        q3.pop();
    }
}

void Conveyor::find_mean(size_t n_tasks)
{
    size_t task_num = 0;

    while (!this->q1.empty())
    {
        std::shared_ptr<Standardizer> task = q1.front();
        task->out1 = system_clock::now();
        task->find_mean(++task_num);

        q2.push(task);
        task->in2 = system_clock::now();
        q1.pop();
    }
}

void Conveyor::find_std_dev()
{
    size_t task_num = 0;

    do
    {
        if (!this->q2.empty())
        {
            std::shared_ptr<Standardizer> task = q2.front();
            task->out2 = system_clock::now();
            task->find_std_dev(++task_num);

            q3.push(task);
            task->in3 = system_clock::now();
            q2.pop();
        }
    } while(!q1.empty() || !q2.empty());
}

void Conveyor::transform()
{
    size_t task_num = 0;

    do
    {
        if (!this->q3.empty())
        {
            std::shared_ptr<Standardizer> task = q3.front();
            task->out3 = system_clock::now();
            task->transform(++task_num);
            tasks.push_back(task);
            task->out_system = system_clock::now();
            q3.pop();
        }
    } while (!q1.empty() || !q2.empty() || !q3.empty());
}

void Conveyor::make_stats(size_t n_tasks)
{
    std::printf("\n\n\n########################### STATISTICS (in ms) ###########################\n");
    int time_q1_min = this->time_dif(tasks[0]->in1, tasks[0]->out1, 'T');
    int time_q1_max = time_q1_min;
    int time_q1_mean = 0;

    int time_q2_min = this->time_dif(tasks[0]->in2, tasks[0]->out2, 'T');
    int time_q2_max = time_q2_min;
    int time_q2_mean = 0;

    int time_q3_min = this->time_dif(tasks[0]->in3, tasks[0]->out3, 'T');
    int time_q3_max = time_q3_min;
    int time_q3_mean = 0;

    int time_system_min = this->time_dif(tasks[0]->in1, tasks[0]->out_system, 'T');
    int time_system_max = time_system_min;
    int time_system_mean = 0;

    int time_queue_min = time_q1_min + time_q2_min + time_q3_min;
    int time_queue_max = time_queue_min;
    int time_queue_mean = 0;

    for (size_t i = 0; i < n_tasks; i++)
    {
        int time_q1_cur = this->time_dif(tasks[i]->in1, tasks[i]->out1, 'T');
        int time_q2_cur = this->time_dif(tasks[i]->in2, tasks[i]->out2, 'T');
        int time_q3_cur = this->time_dif(tasks[i]->in3, tasks[i]->out3, 'T');
        int time_system_cur = this->time_dif(tasks[i]->in1, tasks[i]->out_system, 'T');
        int time_queue_cur = time_q1_cur + time_q2_cur + time_q3_cur;


        if (time_q1_cur < time_q1_min)
            time_q1_min = time_q1_cur;
        if (time_q1_cur > time_q1_max)
            time_q1_max = time_q1_cur;
        time_q1_mean += time_q1_cur;

        if (time_q2_cur < time_q2_min)
            time_q2_min = time_q2_cur;
        if (time_q2_cur > time_q2_max)
            time_q2_max = time_q2_cur;
        time_q2_mean += time_q2_cur;

        if (time_q3_cur < time_q3_min)
            time_q3_min = time_q3_cur;
        if (time_q3_cur > time_q3_max)
            time_q3_max = time_q3_cur;
        time_q3_mean += time_q3_cur;

        if (time_system_cur < time_system_min)
            time_system_min = time_system_cur;
        if (time_system_cur > time_system_max)
            time_system_max = time_system_cur;
        time_system_mean += time_system_cur;


        if (time_queue_cur < time_queue_min)
            time_queue_min = time_queue_cur;
        if (time_queue_cur > time_queue_max)
            time_queue_max = time_queue_cur;
        time_queue_mean += time_queue_cur;
    }

    for (int i = 0; i < n_tasks; i++)
    {
        tasks.pop_back();
    }

    time_q1_mean /= n_tasks;
    time_q2_mean /= n_tasks;
    time_q3_mean /= n_tasks;
    time_system_mean /= n_tasks;
    time_queue_mean /= n_tasks;


    std::printf("Time in q1: min=%10u, max=%10u, mean=%10u\n",
                time_q1_min, time_q1_max, time_q1_mean);
    std::printf("Time in q2: min=%10u, max=%10u, mean=%10u\n",
                time_q2_min, time_q2_max, time_q2_mean);
    std::printf("Time in q3: min=%10u, max=%10u, mean=%10u\n",
                time_q3_min, time_q3_max, time_q3_mean);
    std::printf("Total time in queue: min=%10u, max=%10u, mean=%10u\n",
                time_queue_min, time_queue_max, time_queue_mean);
    std::printf("Total time in system: min=%10u, max=%10u, mean=%10u\n",
                time_system_min, time_system_max, time_system_mean);

    std::printf("########################### ENS OF STATISTICS ###########################\n\n\n");
}

int Conveyor::time_dif(system_clock::time_point begin, system_clock::time_point end, char t)
{
    system_clock::duration tp_begin = begin.time_since_epoch();
    tp_begin -= duration_cast<seconds>(tp_begin);
    time_t tt_begin = system_clock::to_time_t(begin);
    tm t_begin = *gmtime(&tt_begin);

    system_clock::duration tp_end = end.time_since_epoch();
    tp_end -= duration_cast<seconds>(tp_end);
    time_t tt_end = system_clock::to_time_t(end);
    tm t_end = *gmtime(&tt_end);

    int h_dur = t_end.tm_hour - t_begin.tm_hour;
    int m_dur = t_end.tm_min - t_begin.tm_min;
    int s_dur = t_end.tm_sec - t_begin.tm_sec;
    system_clock::duration ms = tp_end - tp_begin;
    int ms_dur = static_cast<unsigned>(ms / milliseconds(1));
    int ms_total = ms_dur + 1000 * (s_dur + 60 * (m_dur + 60 * h_dur));

    switch (t) {
    case 'h':
        return h_dur;
        break;
    case 'm':
        return m_dur;
        break;
    case 's':
        return s_dur;
        break;
    case '1':
        return ms_dur;
        break;
    case 'T':
        return ms_total;
        break;
    default:
        break;
    }
}


