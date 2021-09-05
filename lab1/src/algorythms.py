from copy import deepcopy

DEBUG = False


def lowenstein_dist_matrix_classic(str1, str2):
    # +1 because of an empty string
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[0 for i in range(m)] for j in range(n)]  # MATCH

    # fill with trivial rules
    for i in range(1, n):
        matrix[i][0] = i  # DELETION
    for j in range(1, m):
        matrix[0][j] = j  # INSERTION

    # fill the rest of the matrix
    for i in range(1, n):
        for j in range(1, m):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            replacement = matrix[i - 1][j - 1] + int(str1[i - 1] != str2[j - 1])

            matrix[i][j] = min(insertion, deletion, replacement)

    if DEBUG:
        print('lowenstein_dist_matrix_classic')
        for line in matrix:
            print(line)

    return matrix[n - 1][m - 1]


def lowenstein_dist_matrix_optimized(str1, str2):
    # +1 because of an empty string
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[0 for i in range(m)] for j in range(2)]  # MATCH

    # fill with trivial rules
    for j in range(1, m):
        matrix[0][j] = j  # INSERTION

    # fill the rest of the matrix
    for i in range(1, n):
        matrix[1][0] = i
        for j in range(1, m):
            insertion = matrix[1][j - 1] + 1
            deletion = matrix[0][j] + 1
            replacement = matrix[0][j - 1] + int(str1[i - 1] != str2[j - 1])

            matrix[1][j] = min(insertion, deletion, replacement)

        matrix[0] = deepcopy(matrix[1])

    if DEBUG:
        print('lowenstein_dist_matrix_optimized')
        for line in matrix:
            print(line)

    return matrix[0][m - 1]


def lowenstein_dist_recursion_classic(str1, str2):
    # trivial rules
    if not str1:
        return len(str2)
    elif not str2:
        return len(str1)

    insertion = lowenstein_dist_recursion_classic(str1, str2[:-1]) + 1
    deletion = lowenstein_dist_recursion_classic(str1[:-1], str2) + 1
    replacement = lowenstein_dist_recursion_classic(str1[:-1], str2[:-1]) + int(str1[-1] != str2[-1])

    return min(insertion, deletion, replacement)


def lowenstein_dist_recursion_optimized(str1, str2):
    def _lowenstein_dist_recursion_optimized(str1, str2, matrix):
        len1 = len(str1)
        len2 = len(str2)

        # trivial rules
        if not len1:
            matrix[len1][len2] = len2
        elif not len2:
            matrix[len1][len2] = len1
        else:
            # insertion
            if matrix[len1][len2 - 1] == -1:
                _lowenstein_dist_recursion_optimized(str1, str2[:-1], matrix)
            # deletion
            if matrix[len1 - 1][len2] == -1:
                _lowenstein_dist_recursion_optimized(str1[:-1], str2, matrix)
            # replacement
            if matrix[len1 - 1][len2 - 1] == -1:
                _lowenstein_dist_recursion_optimized(str1[:-1], str2[:-1], matrix)

            matrix[len1][len2] = min(matrix[len1][len2 - 1] + 1,
                                     matrix[len1 - 1][len2] + 1,
                                     matrix[len1 - 1][len2 - 1] + int(str1[-1] != str2[-1]))

        return

    # +1 because of an empty string
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[-1 for i in range(m)] for j in range(n)]
    _lowenstein_dist_recursion_optimized(str1, str2, matrix)

    return matrix[n - 1][m - 1]


def damerau_lowenstein_dist_recursion(str1, str2):
    # trivial rules
    if not str1:
        return len(str2)
    elif not str2:
        return len(str1)

    insertion = lowenstein_dist_recursion_classic(str1, str2[:-1]) + 1
    deletion = lowenstein_dist_recursion_classic(str1[:-1], str2) + 1
    replacement = lowenstein_dist_recursion_classic(str1[:-1], str2[:-1]) + int(str1[-1] != str2[-1])

    if len(str1) > 1 and len(str2) > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        xchange = lowenstein_dist_recursion_classic(str1[:-2], str2[:-2]) + int(str1[-1] != str2[-1])
        return min(insertion, deletion, replacement, xchange)
    else:
        return min(insertion, deletion, replacement)


if __name__ == '__main__':
    str1 = 'ac'
    str2 = 'а'
    x = lowenstein_dist_matrix_optimized(str1, str2)
    print(x)
