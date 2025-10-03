# macdonald.py

# prints the lyrics to Ol' MacDonald had a farm for different animals
def printlyrics(
    *animals: str,
    **animalsounds: str,
):
    for animal in animals:
        print(
            f"""
                Ol' MacDonald had a farm, Ee-igh, Ee-igh, Oh!
                And on that farm he had a {animal}, Ei-igh, Ee-igh, Oh!
                With a {animalsounds[animal]}, {animalsounds[animal]}, here and a {animalsounds[animal]}, {animalsounds[animal]} there.
                Here a {animalsounds[animal]}, there a {animalsounds[animal]}, everywhere a {animalsounds[animal]}, {animalsounds[animal]}.
                Ol' MacDonald had a farm, Ee-igh, Ee-igh, Oh!
            """
        )


# program main entry point
def main():
    # The sounds are from https://www.animalsoundsforkids.com/
    animalsounds = {
        "cow": "moo",
        "pig": "oink",
        "horse": "neigh",
        "goat": "bleat",
        "rooster": "crow",
        "chicken": "cluck",
        "duck": "quack",
        "swan": "song",
        "turkey": "gobble",
        "llama": "call",
        "bison": "grunt",
        "ox": "bellow",
    }

    printlyrics("cow", "pig", "horse", "goat", "rooster", **animalsounds)


if __name__ == "__main__":
    main()
