from sympy import solve, Symbol


def solvecubicformula(
    a: int | float, b: int | float, c: int | float, d: int | float
) -> list[str]:
    x = Symbol("x")
    return solve(a * x**3 + b * x**2 + c * x + d)
