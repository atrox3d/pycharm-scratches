# https://stackabuse.com/python-how-to-flatten-list-of-lists/

def numbers(_from, to):
    for n in range(_from, to+1):
        yield n


regular_generators = [numbers(1, 4), numbers(5, 7), numbers(8, 9)]
flat_list = [item for sublist in regular_generators for item in sublist]
print(flat_list)


