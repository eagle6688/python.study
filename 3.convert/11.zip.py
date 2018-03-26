a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]

zipped_ab = zip(a, b)
print(list(zipped_ab))

zipped_ac = zip(a, c)
print(list(zipped_ac))

unzipped = zip(*zip(a, b))
print(list(unzipped))

x, y = zip(*zip(a, b))
print(x, y)
