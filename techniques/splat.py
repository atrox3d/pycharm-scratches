from dataclasses import dataclass


@dataclass
class CopyResults:
    source = None
    dest = None
    buffer_size = None
    filemode = None
    loops = None
    start = None
    end = None
    elapsed = None

    def __str__(self):
        return f'{self.__class__.__name__}{*[f"{k}={v}" for k, v in vars(self).items()],}'


cr = CopyResults()
cr.loops = 1
print(cr.loops, cr, vars(cr))
