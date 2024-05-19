from sympy import *

Px, Py, Pz = symbols('Px Py Pz')
dx, dy, dz = symbols('dx dy dz')
Ax, Ay, Az = symbols('Ax Ay Az')
ABx, ABy, ABz = symbols('ABx ABy ABz')
ACx, ACy, ACz = symbols('ACx ACy ACz')

t, u, v = symbols('t u v')

solution = solve([

    Px + t * dx - (Ax + ABx * u + ACx * v),
    Py + t * dy - (Ay + ABy * u + ACy * v),
    Pz + t * dz - (Az + ABz * u + ACz * v)

    ], (t, u, v))

print(pycode(solution))

#div = ABx*ACy*dz - ABx*ACz*dy - ABy*ACx*dz + ABy*ACz*dx + ABz*ACx*dy - ABz*ACy*dx

collect(ABx * ACy * dz - ABx * ACz * dy - ABy * ACx * dz + ABy * ACz * dx + ABz * ACx * dy - ABz * ACy * dx, (dx, dy, dz))
div = dx* (ABy * ACz - ABz * ACy) + dy * (ABz * ACx - ABx * ACz) + dz * (ABx * ACy - ABy * ACx)
