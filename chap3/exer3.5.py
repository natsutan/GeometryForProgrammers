from sympy import *

Px1, Px2, Px3, Px4 = symbols('Px1 Px2 Px3 Px4')
dx1, dx2, dx3, dx4 = symbols('dx1 dx2 dx3 dx4')
t = symbols('t')

i, j, k = symbols('i j k')

solution = solve([
    Px1 + t * dx1 - i,
    Px2 + t * dx2 - j,
    Px3 + t * dx3 - k,
    Px4 + t * dx4 - 0

], (t, i, j, k))

print(pycode(solution))


def check(px1, px2, px3, px4, dx1, dx2, dx3, dx4):
    if dx4 == 0:
        print('false')
        return

    i = (px1 * dx4 - px4 * dx1) / dx4
    j = (px2 * dx4 - px4 * dx2) / dx4
    k = (px3 * dx4 - px4 * dx3) / dx4
    t = -px4 / dx4

    if 0 <= t and 0 <= i <= 1 and 0 <= j <= 1 and 0 <= k <= 1:
        print('true')
    else:
        print('false')


check(0.5, 0.5, 0.5, 1, 0, 0, 0, -1)
check(0.5, 0.5, 0.5, 1, 0, 0, 0, 1)
check(0.5, 0.5, 0.5, 1, 1, 0, 0, 0)
check(0.5, 0.5, 0.5, 1, 1, 0, 0, -2)
