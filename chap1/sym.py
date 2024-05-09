from sympy import *

Va, Vp = symbols('Va Vp')

# = 0の形で式を書く
solution = solve([
    Vp - Va * 2,
    Va * 1 + Vp * 1 - 450
], (Va, Vp))

print(solution)

Va, Vp, Vpx, D, t = symbols('Va Vp Vpx D t')

solution = solve([
    Vp - Va * Vpx,
    Va * t + Vp * t - D
], (Va, Vp))

print(solution)
print(rust_code(solution))
