# https://realpython.com/python-zip-function/

letters = list('abcd')                      # convert string to list of chars
print(letters)                              # ['a', 'b', 'c', 'd']

numbers = list(str(1234))                   # convert number to stringd and then list of chars
print(numbers)                              # ['1', '2', '3', '4']
numbers = list(map(int, numbers))           # convert list of chars to list of int
print(numbers)                              # [1, 2, 3, 4]

pairs = list(zip(letters, numbers))         # zip the two lists
print(pairs)                                # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

d = {}                                      # empty dict
for k, v in pairs:                          # loop over tuples
    d[k] = v                                # set element
print(d)                                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d = {}                                      # empty dict
for item in pairs:                          # loop over tuples
    d.update([item])                        # set element from iterable of tuple(s)
print(d)                                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d = dict()                                  # empty dict
d.update(pairs)                             # add dict items from iterable of tuples
print(d)                                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print()
#
#   does not zip anithing, because zip gets only one iterable containing the tuples
#
print(list(d.items()))                      # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(list(zip(d.items())))                 # [(('a', 1),), (('b', 2),), (('c', 3),), (('d', 4),)]
print(*(zip(d.items())))                    # (('a', 1),) (('b', 2),) (('c', 3),) (('d', 4),)
print()
#
#   unpacking items() creates 4 tuples that can be zipped
#
print(*d.items())                           # ('a', 1) ('b', 2) ('c', 3) ('d', 4)
print(list(zip(*d.items())))                # [('a', 'b', 'c', 'd'), (1, 2, 3, 4)]
print(*list(zip(*d.items())))               # ('a', 'b', 'c', 'd') (1, 2, 3, 4)
print()
print(list(d.items()))
print()
#
#   zipping two dictionaries does not
#
doublezip = zip(d.items(), d.items())       # zip two dict (from the same dict)
listdoublezip = list(doublezip)             # create a list from zip
print(type(listdoublezip))                  # <class 'list'>
print(listdoublezip)                        # [(('a', 1), ('a', 1)), (('b', 2), ('b', 2)), (('c', 3), ('c', 3)), (('d', 4), ('d', 4))]
print(*listdoublezip)                       # unpack list to get 4 tuples
                                            # (('a', 1), ('a', 1)) (('b', 2), ('b', 2)) (('c', 3), ('c', 3)) (('d', 4), ('d', 4))

for x in listdoublezip:                     # iterate over list of 4 tuples
    print(type(x), x)                       # <class 'tuple'> (('a', 1), ('a', 1))
                                            # <class 'tuple'> (('b', 2), ('b', 2))
                                            # <class 'tuple'> (('c', 3), ('c', 3))
                                            # <class 'tuple'> (('d', 4), ('d', 4))
print()

doublezip = zip(d.items(), d.items())
print(doublezip)                            # <zip object at 0x000001768500D340>
try:
    for x, y, k, v in doublezip:
        print(x, y, k, v)                       # no output
except Exception as e:
    print(type(e).__name__, e)                  # ValueError not enough values to unpack (expected 4, got 2)

print()

doublezip = zip(d.items(), d.items())
# print(doublezip)                            # <zip object at 0x000001768500D340>
for x, y in doublezip:
    print(x, y)                             # ('a', 1) ('a', 1)
                                            # ('b', 2) ('b', 2)
                                            # ('c', 3) ('c', 3)
                                            # ('d', 4) ('d', 4)
print()

doublezip = zip(d.items(), d.items())
print(doublezip)                            # <zip object at 0x000001768500D340>
for (x, y), (k, v) in doublezip:
    print(x, y, k, v)                       # a 1 a 1
                                            # b 2 b 2
                                            # c 3 c 3
                                            # d 4 d 4
print()
l1 = list(d.items())
l2 = list(d.items())
print(l1, l2, sep='\n')
zipped = zip(l1, l2)
lzipped = list(zipped)
print(lzipped)
print(len(lzipped))
for pair in lzipped:
    print(pair)