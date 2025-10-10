from math import ceil as ceiling, floor


def listsum(l: list) -> int:
    s = 0

    for item in l:
        s += item

    return s


def _2_2(*args: int):

    # 2.2.1
    print("Number of values", len(args))

    # 2.2.2
    maxval = int(0)

    for arg in args[1 : len(args)]:
        if arg > maxval:
            maxval = arg

    print("Max value (index >= 1):", maxval)

    # 2.2.3
    print(
        "Average value (index >= 1):",
        "%g" % (listsum(args[1 : len(args)]) / (len(args) - 1)),
    )

    # 2.2.4
    median: int

    median_position: int

    if len(args[1 : len(args)]) % 2 == 0:
        median_position = len(args) / 2
        median = (args[floor(median_position)] + args[ceiling(median_position)]) / 2
    else:
        median_position = (len(args) + 1) / 2
        median = args[int(median_position)]

    print("Median (index >= 1):", "%g" % (median))


def main():
    loop_should_break = False
    l = []

    while not loop_should_break:
        inp = input("Number: ")
        if not inp == ":q":
            n = int(inp)
            l.append(n)
        else:
            loop_should_break = True

    _2_2(*l)


if __name__ == "__main__":
    main()
