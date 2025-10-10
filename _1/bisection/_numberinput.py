def numberinput(varname: str = None) -> int | float:
    "`number_input` returns an int or float or throws a ValueError"

    number: int | float = None

    while not number:
        if varname:
            inp = input(f"{varname}: ")
        else:
            inp = input("Enter a number: ")
        try:
            try:
                number = int(inp)
            except ValueError:
                number = float(inp)
        except ValueError:
            print("ValueError")

    return number
