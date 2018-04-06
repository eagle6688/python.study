# tuple
tuple = ('Hello', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

# Sub tuple
print('\n')
print('Sub tuple'.center(50, '*'))

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])

# Repeat
print('\n')
print('Repeat'.center(50, '*'))
print(tinytuple * 2)

# Concat
print('\n')
print('Concat'.center(50, '*'))
print(tuple + tinytuple)
