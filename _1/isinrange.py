# isinrange.py


# isinrange returns the sum of the first n natural numbers
def isinrange(n: int | float, start: int | float, stop: int | float) -> bool:
    return True if start <= n <= stop else False


def main():
    n: int | float = None
    start: int | float = None
    stop: int | float = None

    while not n:
        inp = input("n: ")
        try:
            try:
                n = int(inp)
            except ValueError:
                n = float(inp)
        except ValueError:
            print("ValueError")

    while not start:
        inp = input("start: ")
        try:
            try:
                start = int(inp)
            except ValueError:
                start = float(inp)
        except ValueError:
            print("ValueError")

    while not stop:
        inp = input("stop: ")
        try:
            try:
                stop = int(inp)
            except ValueError:
                stop = float(inp)
        except ValueError:
            print("ValueError")

    if isinrange(n=n, start=start, stop=stop):
        print(f"{n} is in the range {start}–{stop} ({start} ≤ {n} ≤ {stop})")

    else:
        print(f"{n} is not in the range {start}–{stop}")


if __name__ == "__main__":
    main()
