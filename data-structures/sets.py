import hashlib

available: set = hashlib.algorithms_available
guaranteed: set = hashlib.algorithms_guaranteed

lavailable = sorted(list(available))
lguaranteed = sorted(list(guaranteed))

print(f"{len(lavailable)=}\n{lavailable=}")
print()
print(f"{len(lguaranteed)=}\n{lguaranteed=}")
print()

difference = available.symmetric_difference(guaranteed)
ldifference = sorted(list(difference))
print(f"{len(ldifference)=}\n{ldifference=}")

print()
for al in lavailable:
    if al in guaranteed:
        print(f"{al:15} [X]")
    else:
        print(f"{al:15} [ ]")
