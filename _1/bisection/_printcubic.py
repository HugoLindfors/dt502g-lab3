def printcubic(
    a: int | float,
    b: int | float,
    c: int | float,
    d: int | float,
    x: int | float | str = "x",
    *args: str,
    **kwargs: str,
):
    "`printcubic` prints a cubic function"
    asgn = "-" if a < 0 else ""
    bsgn = "-" if b < 0 else "+"
    csgn = "-" if c < 0 else "+"
    dsgn = "-" if d < 0 else "+"

    astr = str(a)[1 : len(str(a))] if a < 0 else a
    bstr = str(b)[1 : len(str(b))] if b < 0 else b
    cstr = str(c)[1 : len(str(c))] if c < 0 else c
    dstr = str(d)[1 : len(str(d))] if d < 0 else d

    if int(astr) == 1:
        astr = ""
    else:
        astr = f"{astr}⋅"
    if int(bstr) == 1:
        bstr = ""
    else:
        bstr = f"{bstr}⋅"
    if int(cstr) == 1:
        cstr = ""
    else:
        cstr = f"{cstr}⋅"

    if kwargs.get("func", None) and kwargs.get("s", None) is not None:
        print(
            f"{kwargs["func"]} = {asgn}{astr}{x}³ {bsgn} {bstr}{x}² {csgn} {cstr}{x} {dsgn} {dstr} = {kwargs["s"]}"
        )
    elif kwargs.get("func", None):
        print(
            f"{kwargs["func"]} = {asgn}{astr}{x}³ {bsgn} {bstr}{x}² {csgn} {cstr}{x} {dsgn} {dstr}"
        )
    elif kwargs.get("s", None) is not None:
        print(
            f"{asgn}{astr}{x}³ {bsgn} {bstr}{x}² {csgn} {cstr}{x} {dsgn} {dstr} = {kwargs["s"]}"
        )
    else:
        print(f"{asgn}{astr}{x}³ {bsgn} {bstr}{x}² {csgn} {cstr}{x} {dsgn} {dstr}")
