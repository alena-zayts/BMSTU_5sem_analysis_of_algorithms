#include "slau_solver.h"

// Создание условия
//Problem::Problem()
//{
//    for (int i = 0; i < N; i++)
//    {
//        this->b[i] = i + 1;
//        for (int j = 0; j < N; j++)
//        {
//            this->a[i][j] = i * N + j;
//        }
//    }
//}

Determinant::Determinant(int **matr, int n)
{
    for (int i = 0; i < N; i++)
    {
        this->b[i] = i + 1;
        for (int j = 0; j < N; j++)
        {
            this->a[i][j] = i * N + j;
        }
    }
}

//вычисление определителя
double det(double **matrix, int n) //квадратная матрица размера n*n
{
    double **B = clone(matrix, n);
    //приведение матрицы к верхнетреугольному виду
    for(int step = 0; step < n - 1; step++)
        for(int row = step + 1; row < n; row++)
        {
            double coeff = -B[row][step] / B[step][step]; //метод Гаусса
            for(int col = step; col < n; col++)
                B[row][col] += B[step][col] * coeff;
        }
    //Рассчитать определитель как произведение элементов главной диагонали
    double Det = 1;
    for(int i = 0; i < n; i++)
        Det *= B[i][i];
    //Очистить память
    clear(B, n);
    return Det;
}

// Вычисление мощности движка (a^x)
InverseMatrix::InverseMatrix()
{
    double det = 0;

    this->engine_power = a;

    for (int i = 0; i < x; i++)
    {
        this->engine_power *= a;
    }
}

// Вычисление числа колес (n-ое число Фибоначчи)
Wheels::Wheels(int n)
{
    size_t f1 = 1, f2 = 1;
    this->wheels_cnt = f1;

    for (int i = 2; i < n; i++)
    {
        this->wheels_cnt = f1 + f2;
        f1 = f2;
        f2 = this->wheels_cnt;
    }
}

void SlauSolver::create_engine(size_t task_num)
{
    Logger::log_current_event(task_num, "Part 2 | Start");

    if (this->carcass->is_freight)
    {
        this->engine = std::unique_ptr<InverseMatrix>(new InverseMatrix(10, 150000));
    }
    else
    {
        this->engine = std::unique_ptr<InverseMatrix>(new InverseMatrix(5,  150000));
    }

    Logger::log_current_event(task_num, "Part 2 | End  ");
}

void SlauSolver::create_carcass(size_t task_num)
{
    Logger::log_current_event(task_num, "Part 1 | Start");
    this->carcass = std::unique_ptr<Problem>(new Problem(27644437));
    Logger::log_current_event(task_num, "Part 1 | End  ");
}

void SlauSolver::create_wheels(size_t task_num)
{
    Logger::log_current_event(task_num, "Part 3 | Start");
    this->wheels = std::unique_ptr<Wheels>(new Wheels(this->engine->engine_power));
    Logger::log_current_event(task_num, "Part 3 | End  ");
}
