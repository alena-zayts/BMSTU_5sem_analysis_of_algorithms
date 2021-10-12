
def solve_gauss():
    n = 3                                           # 1
    a = [[1, 0, 1, 3],                              # 2
         [0, 1, 2, 4],
         [1, 1, 1, 5]]

    x = []                                          # 3
    for i in range(n):                              # 4
        x.append(0)                                 # 5

    for i in range(n - 1):                          # 6
        for j in range(i + 1, n):                   # 7
            ratio = a[j][i] / a[i][i]               # 8
            for k in range(n + 1):                  # 9
                sub = ratio * a[i][k]               # 10
                a[j][k] -= sub                      # 11 дальше гаверное от этого а не а, и то же от x

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]        # 12

    for i in range(n - 2, -1, -1):                  # 13
        x[i] = a[i][n]                              # 14
        for j in range(i + 1, n):                   # 15
            sub = a[i][j] * x[j]                    # 16
            x[i] -= sub                             # 17

        x[i] /= a[i][i]                             # 18

    return x

if __name__ == '__main__':
    x = solve_gauss()
    print(x)
