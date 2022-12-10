def banner(text, emptylines=0, char="#", width=80):
    # top line
    print(char * width)

    # top empty lines
    for el in range(int(emptylines / 2) if emptylines else 0):
        print(f"{char}{'':^{width - 2}}{char}")

    if isinstance(text, str):
        text = text.split("\n")
    else:
        try:
            iter(text)
        except TypeError:
            text = (text, )
    # text lines
    for textline in text:
        print(f"{char}{textline:^{width - 2}}{char}")

    # bottom empty lines
    for el in range(int(emptylines / 2) if emptylines else 0):
        print(f"{char}{'':^{width - 2}}{char}")

    # bottom line
    print(char * width)


# banner("hellox\ntest".split('\n'), emptylines=4)
# banner("hellox\ntest", emptylines=4)
# banner(1, emptylines=4)
# banner((1, 2, 3), emptylines=4)
banner("sposta appuntamento")