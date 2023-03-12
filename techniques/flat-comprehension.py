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
nested_list = [[val for val in range(rnd.randint(1, 5))] for rep in range(rnd.randint(1, 5))]
print(f'{nested_list=}')

flat_list = [item for sublist in nested_list for item in sublist]
print(f'{flat_list=}')
