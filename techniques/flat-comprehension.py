import random as rnd

# dynamic random sublists, for-loop version
lst = []
reps = 5
for rep in range(reps):
    sublst = []
    for val in range(rnd.randint(1, 5)):
        sublst.append(val)
    lst.append(sublst)
print(lst)


# dynamic random sublists, comprehension version
print(
    [[val for val in range(rnd.randint(1, 5))] for rep in range(rnd.randint(1, 5))]
)
