# sumncubes.py


# sumncubes returns the sum of the first n natural numbers
def sumncubes(n: int) -> int:

    s = int(0)

    while n > 0:
        s += n**3
        n -= 1

    return s


def main():
    n: int = None
    while not n:
        try:
            n = int(input("n: "))
            s = sumncubes(n)
            print(s)
        except ValueError:
            print("ValueError")


if __name__ == "__main__":
    main()
