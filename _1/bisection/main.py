from os import system as cmd

from _numberinput import numberinput
from _printcubic import printcubic
from _solvecubicformula import solvecubicformula


def newline(n=1):
    "newline adds a desired number of blank rows, default is 1"
    while abs(n) > 0:
        print()
        n -= 1


def main():
    "program main entry point"

    cmd("clear")

    newline(2)

    print("Try a = 1, b = -6, c = 11, d = -6")

    newline()

    a = numberinput("a")
    b = numberinput("b")
    c = numberinput("c")
    d = numberinput("d")

    newline()

    printcubic(a, b, c, d, func="f(x)")
    print("f(x) = 0")
    printcubic(a, b, c, d, s=0)

    newline()

    solutions = solvecubicformula(a, b, c, d)

    for i, solution in enumerate(solutions):
        try:
            # Native Python doesn't understand sqrt(), therefore we must import it from math or define it ourselves
            solution = eval(
                f"""
                    def sqrt(n: float) -> float:
                        return n**(1/2)
                    {solution}
                """
            )
            print(f"x_{i + 1} =", solution)
        except:
            print(f"x_{i + 1} =", solution)

    newline()


if __name__ == "__main__":
    main()
