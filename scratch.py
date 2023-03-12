numbers = list(range(13))
print(numbers)

letters = list("ABC")
print(letters)

letters = letters * (int((len(numbers) / len(letters))) + 1)
print(letters)

print(list(zip(letters, numbers)))