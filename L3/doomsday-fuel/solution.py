from fractions import Fraction, gcd


def least_common_multiple(l):
    lcm = 1
    for el in l:
        lcm = lcm*el//gcd(lcm, el)
    return lcm


def matmul(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for k in range(len(b[0])):
            row_sum = []
            for j in range(len(b)):
                row_sum.append(a[i][j] * b[j][k])
            row.append(sum(row_sum))
        result.append(row)
    return result


def transpose(a):
    for i in range(len(a)):
        for j in range(i, len(a[0])):
            if i == j:
                continue
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


def get_sub_matrix(a, i, j):
    return [[element for element in row[:j] + row[j+1:]] for row in a[:i] + a[i+1:]]


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    elif len(a) == 2:
        return a[0][0]*a[1][1] - a[0][1]*a[1][0]

    det = 0
    for j in range(len(a[0])):
        sub_matrix = get_sub_matrix(a, 0, j)
        det += (-1)**j*a[0][j] * determinant(sub_matrix)

    return det


def inverted(a):
    cofactor = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            sub_matrix = get_sub_matrix(a, i, j)
            sub_det = determinant(sub_matrix)
            row.append((-1)**(i + j)*sub_det)
        cofactor.append(row)

    det = float(determinant(a))
    inverse = transpose(cofactor)
    for i in range(len(inverse)):
        for j in range(len(inverse[0])):
            inverse[i][j] /= det
    return inverse


def normalize(a):
    return [[element / float(sum(row)) for element in row] for row in a]


def get_f(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j:
                a[i][j] = 1 - a[i][j]
            else:
                a[i][j] = -a[i][j]

    return a


def get_r_q(a):
    terminal_states = list()
    non_terminal_states = list()
    for i, row in enumerate(a):
        terminal = True
        for no in row:
            if no != 0:
                terminal = False
                break
        if terminal:
            terminal_states.append(i)
            a[i][i] = 1
        else:
            non_terminal_states.append(i)

    one_pos = 0
    for i, state in enumerate(terminal_states):
        a[i], a[state] = a[state], a[i]
        if i == one_pos:
            one_pos = state
        elif state == one_pos:
            one_pos = i
        for row in a:
            row[i], row[state] = row[state], row[i]

    a = normalize(a)
    r = [[element for element in row[:len(
        terminal_states)]] for row in a[len(terminal_states):]]
    q = [[element for element in row[len(
        terminal_states):]] for row in a[len(terminal_states):]]

    return r, q, one_pos - len(terminal_states)


def solution(m):
    if len(m) == 1:
        return [1, 1]

    if sum(m[0]) == 0:
        probabilites = [0] * len(m)
        probabilites[0] = 1
        probabilites.append(1)
        return probabilites

    r, q, one_pos = get_r_q(m)
    f = inverted(get_f(q))
    fr = matmul(f, r)

    probabilites = [Fraction(i).limit_denominator()
                    for i in fr[one_pos]]

    lcm = least_common_multiple(
        [element.denominator for element in probabilites])

    probabilites = [int(round(i * lcm))
                    for i in probabilites]
    probabilites.append(lcm)

    return probabilites
