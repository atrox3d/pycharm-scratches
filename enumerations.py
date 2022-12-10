#
# https://betterprogramming.pub/take-advantage-of-the-enum-class-to-implement-enumerations-in-python-1b65b530e1d
#
from enum import Enum

# Create an Enum class using the functional API
DirectionFunctional = Enum("DirectionFunctional", "NORTH EAST SOUTH WEST")
# Check what the Enum class is
print(f"{DirectionFunctional                     = }")
# Check the items
print(f"{list(DirectionFunctional)               = }")
print(f"{DirectionFunctional.__members__.items() = }")
print()
print()
print()


# Create a function and patch it to the DirectionFunctional class
def angle(self):
    print(f"{id(self) = }")
    right_angle = 90.0
    return right_angle * (self.value - 1)


DirectionFunctional.angle = angle   # monkey patching

# Create a member and access its angle
south = DirectionFunctional.SOUTH
print(f"{id(south)  = }")
print("South Angle:", south.angle())
