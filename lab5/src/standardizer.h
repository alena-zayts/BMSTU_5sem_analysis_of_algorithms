#ifndef __STDANDARDIZER_H__
#define __STDANDARDIZER_H__

#include <memory>
#include <cmath>

#include "logger.h"

class Mean
{
public:
    Mean(int n, double *arr);
    ~Mean() = default;

    double mean;
};

class StdDev
{
public:
    StdDev(int n, double *arr, double mean);
    ~StdDev() = default;

    double std_dev;
};

class Transformer
{
public:
    Transformer(int n, double *arr, double mean, double std_dev, double *new_arr);
    ~Transformer() = default;
};

class Standardizer
{
public:
    Standardizer(int n, double *arr, double *new_arr);
    ~Standardizer() = default;

    void find_mean(size_t task_num);
    void find_std_dev(size_t task_num);
    void transform(size_t task_num);

    system_clock::time_point in1;
    system_clock::time_point out1;
    system_clock::time_point in2;
    system_clock::time_point out2;
    system_clock::time_point in3;
    system_clock::time_point out3;
    system_clock::time_point out_system;

private:
    std::unique_ptr<Mean> meanC;
    std::unique_ptr<StdDev> stdDevC;
    std::unique_ptr<Transformer> transformer;

    int n;
    double *arr;
    double *new_arr;
};

#endif
