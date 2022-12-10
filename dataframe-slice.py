import pandas

# df = pandas.read_csv("path/to/csv")
a = list("ABCDEFG")
b = list(range(1, len(a)))

print(a)
print(b)
data = list(zip(a, b))
print(data)

df = pandas.DataFrame(data, columns=['x', 'y'])
print(df)

for col, _range in zip(["col1", "col2"], [slice(10), slice(10, None)]):
    print(col, _range)
    for index, row in df[_range].iterrows():
        print(col, index, row)

