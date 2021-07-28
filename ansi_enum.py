from enum import Enum

DARK_LIGHT = Enum('DarkLight', "DARK LIGHT", start=0)
FOREGROUND = Enum("Fg", "FG_BLACK FG_RED FG_GREEN FG_YELLOW FG_BLUE FG_MAGENTA FG_CYAN FG_WHITE", start=30)
BACKGROUND = Enum("Bg", "BG_BLACK BG_RED BG_GREEN BG_YELLOW BG_BLUE BG_MAGENTA BG_CYAN BG_WHITE", start=40)

breakpoint()
# light_dict = {f"LIGHT_{name[3:]}": (DarkLight.LIGHT.value, value.value) for name, value in Fg.__members__.items()}
ligh_dict = {f"{name[3:]}": f"\033[{DARK_LIGHT.LIGHT.value};{value.value}m" for name, value in FOREGROUND.__members__.items()}
print(ligh_dict)
#
# darkcolors_dict = {f"DARK_{name[3:]}": (DarkLight.DARK.value, value.value) for name, value in Fg.__members__.items()}
dark_dict = {f"{name[3:]}": f"\033[{DARK_LIGHT.DARK.value};{value.value}m" for name, value in FOREGROUND.__members__.items()}
# print(darkcolors_dict)

ANSI_LIGHT = Enum('AnsiLightColors', ligh_dict)
ANSI_LIGHT.__str__ = lambda self: self._value_

ANSI_DARK = Enum('AnsiDarkColors', dark_dict)
ANSI_DARK.__str__ = lambda self: self._value_

for x in ANSI_LIGHT:
    print(x, x.name, repr(x))

print(ANSI_LIGHT.RED, "red")


for x in ANSI_DARK:
    print(x, x.name, repr(x))

print(ANSI_DARK.RED, "red")

exit()


def toint(self):
    print("toint")
    # for k, v in vars(self).items():
    #     print(k, v)
    return int(self._value_)


def tostr(self):
    print("tostr")
    # for k, v in vars(self).items():
    #     print(k, v)
    return str(self._value_)


FOREGROUND.__int__ = toint
FOREGROUND.__str__ = tostr

for x in FOREGROUND:
    print("x:", x)
    print(f"x={x}")
    print(int(x))
    print()
