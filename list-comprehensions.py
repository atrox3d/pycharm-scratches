#
# https://www.youtube.com/watch?v=3dt4OGnU5sM
#
# Python Tutorial: Comprehensions - How they work and why you should be using them
#
#################################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'{"nums":<10} = {nums}')                         # OUTPUT | nums       = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#################################################################################
# copy list - for loop version
#################################################################################
print("\ncopy nums in my_list, for loop:")
my_list = []
for n in nums:                                          # iterate through source list
    my_list.append(n)                                   # append each element to dest list
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# copy list - list comprehension version
#################################################################################
print("\ncopy nums in my_list, list comprehension: [n for n in nums]")
my_list = [                                             # *** square bracket ***
    n                                                   # appends n to my_list
    for n in nums                                       # iterates through nums
]
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# generate list of squares of n - for loop version
#################################################################################
print("#" * 80)
print("\ngenerate list of squares of nums in my_list, for loop:")
my_list = []
for n in nums:                                          # iterate through source list
    my_list.append(n * n)                               # appends square of n to my_list
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# generate list of squares of n - list comprehension version
#################################################################################
print("\ngenerate list of squares of nums in my_list, list comprehension: [n*n for n in nums]")
my_list = [                                             # *** square bracket ***
    n * n                                               # appends square n to my_list
    for n in nums                                       # iterate through nums
]
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# generate list of squares of n - map + lambda version
#################################################################################
print("\ngenerate list of squares of nums in my_list, map + lambda: map(lambda n: n*n, nums)")
my_list = list(                                         # converts iterator to list
    map(                                                # creates iterator from function
        lambda n: n * n,                                # lambda function: returns square n
        nums                                            # list of arguments, one for each call
    )
)
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# conditional list copy - for loop version
#################################################################################
print("#" * 80)
print("\ngenerate sublist of even elements from nums to my_list, for loop:")
my_list = []
for n in nums:                                          # iterates through nums list
    if not n % 2:                                       # check if even (not 0 == True)
        my_list.append(n)                               # appends to my_list
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# conditional list copy - list comprehension version
#################################################################################
print("\ngenerate sublist of even elements from nums to my_list, list comprehension: [n for n in nums if not n%2]")
my_list = [                                             # *** square bracket ***
    n                                                   # appends n to my_list
    for n in nums                                       # loop through nums
    if not n % 2                                        # assigns n only if even
]
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# conditional list copy - filter + lambda version
#################################################################################
print("\ngenerate list of squares of nums in my_list, filter + lambda: filter(lambda n: n % 2 == 0, nums)")
my_list = list(                                         # converts iterator to list
    filter(                                             # creates iterator from true return
        lambda n: n % 2 == 0,                           # lambda function: true if even
        nums                                            # list of arguments, one for each call
    )
)
print(f'{"my_list":<10} = {my_list}')
#################################################################################
# generate a list of letter, num pairs for each element of abcd 0123
# for loop version
#################################################################################
print("#" * 80)
print("\ngenerate a list of letter, num pairs for each element of abcd 0123, for loop:")
my_list = []
for letter in 'abcd':                                   # a, b, c, d
    for num in range(4):                                # 0, 1, 2, 3
        my_list.append((letter, num))                   # append tuple with combination
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# generate a list of letter, num pairs for each element of abcd 0123
# for loop version
# list comprehension version
#################################################################################
print(
    "\ngenerate a list of letter, num pairs for each element of abcd 0123, list comprehension: [n for n in nums if not n%2]")
my_list = [                                             # *** square bracket ***
    (letter, num)                                       # assigns tuple to my_list
    for letter in 'abcd'                                # a, b, c, d
    for num in range(4)                                 # 0, 1, 2, 3
]
print(f'{"my_list":<10} = {my_list}')

#################################################################################
# generate a dictionary of civilian names of superheroes
#################################################################################
print("#" * 80)
print("\ngenerate a dictionary of civilian names of superheroes, for loop:")
names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heroes = ['batman', 'superman', 'spiderman', 'wolverine', 'deadpool']
print(f'{"names":<10} = {names}')
print(f'{"heroes":<10} = {heroes}')
# OUTPUT | [('bruce', 'batman'), ('clark', 'superman'), ('peter', 'spiderman'), ('logan', 'wolverine'), ('wade', 'deadpool')]
print(list(zip(names, heroes)))

#################################################################################
# for loop version
#################################################################################
my_dict = {}
for name, hero in zip(names, heroes):                   # loop through tuples
    my_dict[name] = hero                                # adds dict item
print(f'{"my_dict":<10} = {my_dict}')

#################################################################################
# dictionary comprehension version
#################################################################################
print(
    "\ngenerate a dictionary of civilian names of superheroes, list comprehension: {name: hero for name, hero in zip(names, heroes)}")
my_dict = {                                             # *** brace ***
    name: hero                                          # adds dict item
    for name, hero in zip(names, heroes)                # loop through iterator
}
print(f'{"my_dict":<10} = {my_dict}')

#################################################################################
# conditional dictionary comprehension version
#################################################################################
print(
    "\ngenerate a dictionary of civilian names of superheroes, list comprehension: {name: hero for name, hero in zip(names, heroes) if name != 'peter'}")
my_dict = {                                             # *** brace ***
    name: hero                                          # adds dict item
    for name, hero in zip(names, heroes)                # loop through iterator
    if name != 'peter'                                  # adds condition
}
print(f'{"my_dict":<10} = {my_dict}')

#################################################################################
# generate a set
#################################################################################
print("#" * 80)
nums = [1, 2, 3, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
print(f'{"nums":<10} = {nums}')

#################################################################################
# for loop version
#################################################################################
print("\ngenerate a set of unique numbers from a list, for loop:")
my_set = set()
for n in nums:
    my_set.add(n)
print(f'{"my_set":<10} = {my_set}')

#################################################################################
# set comprehension version
#################################################################################
print("\ngenerate a set of unique numbers from a list, set comprehension: {n for n in nums}")
my_set = {                                              # *** brace ***
    n                                                   # adds n to set
    for n in nums                                       # loop through list
}
print(f'{"my_set":<10} = {my_set}')

#################################################################################
# generator expressions
#################################################################################
print("#" * 80)
print("# generator expressions")
print("#" * 80)

print("use a generator function to obtain an iterable of square numbers")


def gen_func(nums):                                     # generator function
    for n in nums:                                      # loop through list
        yield n * n                                     # generates next square


my_gen = gen_func(nums)                                 # returns iterable
for n in my_gen:                                        # iterate
    print(n)

print("use a generator expression to obtain an iterable of square numbers, (n * n for n in nums)")
my_gen = (                                              # *** parenthesis ***
    n * n                                               # yields square n
    for n in nums                                       # loops through nums
)

for n in my_gen:
    print(n)

