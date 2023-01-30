from pprint import pprint

# m = [
#     [  # m[0]
#         [  # m[0][0]
#             1, 2, 3  # m[0][0][0:2]
#         ],
#     ],
# ]
# print("m          : ", len(m), m)
# print("m[0]       : ", len(m[0]), m[0])
# print("m[0][0]    : ", len(m[0][0]), m[0][0])
# # print("m[0][0][0] : ", len(m[0][0][0]), m[0][0][0])
# # print("m[0][0][0] : ", len(m[0][0][0]), m[0][0][0])
# # pprint(m)

import numpy as np

# print(f"np.shape(m): {np.shape(m)}")
# print(f"len(np.shape(m)): {len(np.shape(m))}")
# print(f"m[0][0][0:3]: {m[0][0][0:3]}")


def discover(array, reset=False):
    if not hasattr(discover, "dimensions") or reset:        # sets or resets "static" variable
        discover.dimensions = 0
        print("discover | reset dimensions")

    try:
        if type(array) == list:
            discover.dimensions += 1
            print(f"discover | type == list | dimensions | {discover.dimensions} | array | {array}")
            for elem in array:
                print(f"discover | elem | {elem}")
                discover(elem)
                # if len(n):
                #     print(f"discover | len(n) | {len(n)} | n: {n}")
                # if type(n) == list:
                #     discover.dimensions += 1
                #     print(f"discover | dimensions | {discover.dimensions}")
                # for item in elem:
                #     print(f"discover | recurse | {item}")
                #     discover(item)
        else:
            print(f"discover | type == {type(array)}")

    except TypeError as e:
        print(e, type(e))
        # print(f"discover | fail in recurse | {item}")
        return


# discover(m)

ls = []                 # dim 1
ls.append([1, 2, 3])    # dim 2
ls.append([4, 5, 6])    # dim 2
# ls.append([7, 8, 9])

discover(ls, True)
print("ls           | ", ls)
print("shape ls     | ", np.shape(ls))
print("len shape ls | ", len(np.shape(ls)))
pprint(ls)
