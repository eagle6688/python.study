# String
str = "Hello World!"

# Display a subset of String
print('\n')
print('Sub string'.center(50, '*'))

print(str[0])
print(str[2:5])
print(str[2:])
print(str[:5])
print(str[-1])
print(str[-6])
print(str[-6:])

# Repeat
print('\n')
print('Repeat string'.center(50, '*'))

print(str*2)

# Concat
print('\n')
print('Concat string'.center(50, '*'))

print(str + ' Test')

# Escape character
print('\n')
print('Escape character'.center(50, '*'))

print('\n Hello')
print(r'\n Hello')

# Three quotation
print('\n')
print('Three quotation'.center(50, '*'))

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)

# Unicode string
print('\n')
print('Unicode'.center(50, '*'))

print(u'Hello World!')

# capitalize: Uppercase first char, lowercase others
print('\n')
print('capitalize'.center(50, '*'))

print('Hello World!'.capitalize())

# center
print('\n')
print('center'.center(50, '*'))

print(str.center(100, '='))

# count
print('\n')
print('count'.center(50, '*'))

print(errHTML.count('FORM', 0, len(errHTML)))

# encode
print('\n')
print('encode'.center(50, '*'))

encodeStr = '你好, world!'.encode('utf-8')
print(encodeStr)

# decode
print('\n')
print('decode'.center(50, '*'))

decodeStr = encodeStr.decode('utf-8')
print(decodeStr)

# endswith
print('\n')
print('endswith'.center(50, '*'))

print(str.endswith('ld'))
print(str.endswith('ld', 0, len(str) - 1))

# find
print('\n')
print('find'.center(50, '*'))

print(str.find('o'))
print(str.find('o', 5, len(str)))

# format
print('\n')
print('format'.center(50, '*'))

print("My name is %s and weight is %d kg!" % ('Zara', 21))

print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))
print("Website: {name}, url: {url}".format(
    name="Google", url="www.google.com"))

site = {"name": "Google", "url": "www.google.com"}
print("Website: {name}, url: {url}".format(**site))

list = ['Google', 'www.google.com']
print("Website: {0[0]}, url: {0[1]}".format(list))

# index, like 'find' but throw exception when not find
print('\n')
print('index'.center(50, '*'))

print(str.index('Hello'))
# print(str.index('hello')) throw an exception
print(str.index('World'))

# isalnum
print('\n')
print('isalnum'.center(50, '*'))

print(str.isalnum())
print('asd'.isalnum())
print('123'.isalnum())
print(''.isalnum())

# isalpha
print('\n')
print('isalpha'.center(50, '*'))

print('asd'.isalpha())
print('123'.isalpha())
print(''.isalpha())

# isdecimal
print('\n')
print('isdecimal'.center(50, '*'))

print('asd'.isdecimal())
print('123'.isdecimal())
print(u'123'.isdecimal())

# join
print('\n')
print('join'.center(50, '*'))

sequence = ("a", "b", "c")
print('-'.join(sequence))

# lstrip
print('\n')
print('lstrip'.center(50, '*'))

print("     this is string example....wow!!!     ".lstrip())
print("88888888this is string example....wow!!!8888888".lstrip('8'))

# strip
print('\n')
print('strip'.center(50, '*'))

print("     this is string example....wow!!!     ".strip())
print("88888888this is string example....wow!!!8888888".strip('8'))

# replace
print('\n')
print('replace'.center(50, '*'))

print("this is string example....wow!!! this is really string".replace('is', 'was'))
print("this is string example....wow!!! this is really string".replace('is', 'was', 3))

# split
print('\n')
print('split'.center(50, '*'))

print("Line1-abcdef \nLine2-abc \nLine4-abcd".split())
print("Line1-abcdef \nLine2-abc \nLine4-abcd".split(' ', 1))

# splitlines
print('\n')
print('splitlines'.center(50, '*'))

print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(True))

# swapcase
print('\n')
print('swapcase'.center(50, '*'))

print("this is string example....wow!!!".swapcase())
print("THIS IS STRING EXAMPLE....WOW!!!".swapcase())
