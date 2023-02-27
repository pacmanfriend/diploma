import random


def weight_vect_sum(vect_a, vect_b) -> float:
    assert (len(vect_a) == len(vect_b))

    result = 0.0

    for i in range(len(vect_a)):
        result += vect_a[i] * vect_b[i]

    return result


def vect_mult(vect_a, vect_b) -> list:
    assert (len(vect_a) == len(vect_b))

    result = [0.0 for _ in range(len(vect_a))]

    for i in range(len(result)):
        result[i] = vect_a[i] * vect_b[i]

    return result


def scalar_mult(scalar, vect) -> list:
    for v in vect:
        v *= scalar

    return vect


def matrix_sub(matrix_a, matrix_b) -> list[list[float]]:
    assert (len(matrix_a) == len(matrix_b))

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b)):
            matrix_a[i][j] -= matrix_b[i][j]

    return matrix_a


def calc_weight_deltas(vect_a, vect_b) -> list[list]:
    result = [[0.0 for _ in range(len(vect_b))] for _ in range(len(vect_a))]

    for i in range(len(vect_a)):
        for j in range(len(vect_b)):
            result[i][j] = vect_a[i] * vect_b[j]

    return result


def generate_random_matrix(n, m) -> list[list[float]]:
    matrix = [[0.0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            matrix[i][j] = random.random()

    return matrix
