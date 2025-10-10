from os import system as cmd


def clear():
    cmd("clear")


def newline(n=1):
    "newline adds a desired number of blank rows, default is 1"
    while abs(n) > 0:
        print()
        n -= 1


def listproduct(l: list) -> int:

    product = 1

    for item in l:
        product *= item

    return product


def main():
    clear()
    newline(2)

    print("Welcome! Enter :q to quit the loop!")

    newline()

    loop_should_break = False
    l = []

    while not loop_should_break:
        inp = input("Number: ")
        if not inp == ":q":
            n = int(inp)
            l.append(n)
        else:
            loop_should_break = True

    product = listproduct(l=l)

    newline()

    print(f"List product of {l} = {product}")

    if l == []:
        print(
            "Actually, 0! is indeed equal to 1, so, this actually makes perfect sense"
        )

    newline()


if __name__ == "__main__":
    main()
