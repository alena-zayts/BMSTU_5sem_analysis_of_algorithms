#ifndef __CAR_H__
#define __CAR_H__

#include <memory>
#include <cmath>

#include "logger.h"
#define N 5

//class Problem
//{
//public:
//    Problem();
//    ~Problem() = default;

//    int a[N][N];
//    int b[N];
//};

class Determinant
{
public:
    Determinant(double **matr,int n);
    ~Determinant() = default;

    double det;
};

class InverseMatrix
{
public:
    InverseMatrix();
    ~InverseMatrix() = default;

    double ar[N][N];
//private:
//    double find
};

class Wheels
{
public:
    Wheels(int n);
    ~Wheels() = default;

    size_t wheels_cnt;
};

class SlauSolver
{
public:
    SlauSolver() = default;
    ~SlauSolver() = default;

    void create_engine(size_t);
    void create_carcass(size_t);
    void create_wheels(size_t);

private:
    std::unique_ptr<Determinant> determinant;
    std::unique_ptr<InverseMatrix> engine;
    std::unique_ptr<Wheels> wheels;
};

#endif
