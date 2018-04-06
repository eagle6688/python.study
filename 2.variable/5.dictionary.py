# Dictionary
print('\n')
print('Dictionary'.center(50, '*'))

dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
print(dict)

# Change
print('\n')
print('Change'.center(50, '*'))

dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict)

# keys
print('\n')
print('keys'.center(50, '*'))
print(dict.keys())

# values
print('\n')
print('values'.center(50, '*'))
print(dict.values())

# items
print('\n')
print('items'.center(50, '*'))
print(dict.items())

# del
print('\n')
print('del'.center(50, '*'))

del dict['dept']
print(dict)

# clear
print('\n')
print('clear'.center(50, '*'))

dict.clear()
print(dict)

# str
print('\n')
print('str'.center(50, '*'))

dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(str(dict))

# type
print('\n')
print('type'.center(50, '*'))
print(type(dict))

# copy
print('\n')
print('copy'.center(50, '*'))

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # Refer object
dict3 = dict1.copy()  # Shallow copy

dict1['user'] = 'root'
dict1['num'].pop()

print(dict1)
print(dict2)
print(dict3)

# fromkeys
print('\n')
print('fromkeys'.center(50, '*'))

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print(dict)

dict = dict.fromkeys(seq, 10)
print(dict)

# get
print('\n')
print('get'.center(50, '*'))

dict = {'Name': 'Zara', 'Age': 27}
print(dict.get('Name'))
print(dict.get('Sex', 'Never'))

# __contains__
print('\n')
print('__contains__'.center(50, '*'))
print(dict.__contains__('Age'))
print(dict.__contains__('Value'))

# setdefault
print('\n')
print('setdefault'.center(50, '*'))

value = dict.setdefault('ecoom', 'Taobao')
print(value)
print(dict)

# update
print('\n')
print('update'.center(50, '*'))

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}
dict1.update(dict2)
print(dict1)

# pop
print('\n')
print('pop'.center(50, '*'))

value = dict1.pop('Sex')
print(value)

value = dict1.pop('Sex', 'male')
print(value)
