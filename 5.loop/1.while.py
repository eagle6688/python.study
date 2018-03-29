index = 0

while(index < 10):
    print('Current index: ', index)
    index += 1

    if(index < 5):
        continue
    elif (index == 6):
        break
else:
    print('The last index: ', index)

index = 0

while(index < 3):
    print('Current index: ', index)
    index += 1
else:
    print('The last index: ', index)

while (True):
    str = input('Enter a string: ')
    print('You entered: ', str)

    if(str == 'exit'):
        break
