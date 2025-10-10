def number(n: None) -> int | float:
    while not n:
        inp = input("Enter a number: ")
        try:
            try:
                n = int(inp)
            except ValueError:
                n = float(inp)
        except ValueError:
            print("ValueError")

    return n


def maximum(*numbers: int | float) -> int | float:

    m: int | float = 0

    for number in numbers:
        if number > m:
            m = number

    return m


def main():
    l: int | float = None
    m: int | float = None
    n: int | float = None

    l = number(l)
    m = number(m)
    n = number(n)

    print(maximum(l, m, n))


if __name__ == "__main__":
    main()
