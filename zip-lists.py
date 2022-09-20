# https://realpython.com/python-zip-function/

letters = list('abcd')                      # convert string to list of chars
print(letters)                              # ['a', 'b', 'c', 'd']

numbers = list(str(1234))                   # convert number to stringd and then list of chars
print(numbers)                              # ['1', '2', '3', '4']
numbers = list(map(int, numbers))           # convert list of chars to list of int
print(numbers)                              # [1, 2, 3, 4]

pairs = zip(letters, numbers)               # zip the two lists
print(list(pairs))                          # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

pairs = zip(letters, numbers)               # zip the two lists
for x in pairs:                             # parallel loop: tuples
    print(x)                                # ('a', 1)
                                            # ('b', 2)
                                            # ('c', 3)
                                            # ('d', 4)

pairs = zip(letters, numbers)               # zip the two lists
for x, y in pairs:                          # parallel loop: str, int
    print(x, y)                             # a 1
                                            # b 2
                                            # c 3
                                            # d 4

pairs = list(zip(letters, numbers))         # zip the two lists
print(pairs)                                # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(*pairs)                               # ('a', 1), ('b', 2), ('c', 3), ('d', 4)

numbers, letters = zip(*pairs)              # (un)zip pairs to the original arrays
print(numbers, letters, sep='\n')           # ('a', 'b', 'c', 'd')
                                            # (1, 2, 3, 4)







