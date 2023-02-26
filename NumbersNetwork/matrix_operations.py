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


def calc_weight_deltas(vect_a, vect_b) -> list[list]:
    result = [[0.0 for _ in range(len(vect_b))] for _ in range(len(vect_a))]

    for i in range(len(vect_a)):
        for j in range(len(vect_b)):
            result[i][j] = vect_a[i] * vect_b[j]

    return result
