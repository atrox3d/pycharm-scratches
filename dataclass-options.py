from dataclasses import dataclass


@dataclass
class Options:
    pass


options = Options()

options.x = 1

print(options.x)


class Opt:
    # pass
    def __getattr__(self, item):
        return None

opt = Opt()
opt.x = 2

print(opt.x)
print(opt.y)

setattr(opt, "y", 0)
print(opt.y)

