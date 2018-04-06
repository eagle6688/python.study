# list
list = ['Hello', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

# sub
print('\n')
print('Sub list'.center(50, '*'))

print(list)
print(list[0])
print(list[1:3])
print(list[2:])

# value
list[0] = 'Hello World!'

# repeated
print('\n')
print('Repeated'.center(50, '*'))
print(tinylist * 2)

# contat
print('\n')
print('Contat'.center(50, '*'))
print(list + tinylist)

# append
print('\n')
print('append'.center(50, '*'))

tinylist.append('Google')
print(tinylist)

tinylist = tinylist+['Facebook']
print(tinylist)

# del
print('\n')
print('del'.center(50, '*'))

del tinylist[2]
print(tinylist)

# len
print('\n')
print('len'.center(50, '*'))

print(len(list))

# in
print('\n')
print('in'.center(50, '*'))

print('john' in list)
print('Hello' in list)

# for
print('\n')
print('for'.center(50, '*'))

for item in list:
    print(item)

# max
print('\n')
print('max'.center(50, '*'))

list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
# print('Max element of list1: ', max(list1)) throw exception
print('Max element of sub list1: ', max(list1[1:]))
print('Max element of list2: ', max(list2))

# min
print('\n')
print('min'.center(50, '*'))

print('Min element of sub list1: ', min(list1[1:]))
print('Min element of list2: ', min(list2))

# count
print('\n')
print('count'.center(50, '*'))

list3 = [123, 'xyz', 'zara', 'abc', 123]
print('Count for 123: ', list3.count(123))
print('Count for 123: ', list3.count('123'))
print('Count for abc: ', list3.count('abc'))

# extend
print('\n')
print('extend'.center(50, '*'))

list3.extend([2009, 'manni'])
print(list3)

# index
print('\n')
print('index'.center(50, '*'))

print(list3.index('xyz'))
print(list3.index(123))

# insert
print('\n')
print('insert'.center(50, '*'))

list3.insert(2, 'Alibaba')
print(list3)

# pop
print('\n')
print('pop'.center(50, '*'))

lastEle = list3.pop()
print('The removing element: ', lastEle)
print('Current list: \n', list3)

# remove
print('\n')
print('remove'.center(50, '*'))

list3.remove(123)
print(list3)

# reverse
print('\n')
print('reverse'.center(50, '*'))

list3.reverse()
print(list3)

# sort
print('\n')
print('sort'.center(50, '*'))

# list3.sort() throw exception
list2.sort()
print(list2)
