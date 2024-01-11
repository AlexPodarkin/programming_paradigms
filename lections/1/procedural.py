def calculate_x(a0, b0):
    return -b0 / (2 * a0)


def calculate_x1x2(a1, b1, d):
    x1 = (-b1 + d ** 0.5) / (2 * a1)
    x2 = (-b1 - d ** 0.5) / (2 * a1)
    return x1, x2


def calculate_d(a2, b2, c2):
    return b2 ** 2 - 4 * a2 * c2


def solve_for_x(a3, b3, c3):
    d = calculate_d(a3, b3, c3)
    if d > 0:
        return calculate_x1x2(a3, b3, d)
    elif d == 0:
        return calculate_x(a3, b3)
    else:
        return 'No real solutions'


if __name__ == '__main__':
    a, b, c = 6, -17, 12
    solution = solve_for_x(a, b, c)
    print(solution)
