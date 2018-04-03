str = "Hello World!"
print(str)
print(str[0])

# Display a subset of String
print(str[2:5])
print(str[2:])
print(str[:5])
print(str[-1])
print(str[-6])
print(str[-6:])

# Repeat
print(str*2)

# Concat
print(str + ' Test')

# Escape character
print('\n Hello')
print(r'\n Hello')

# Format
print("My name is %s and weight is %d kg!" % ('Zara', 21))

formatedString = "WebSite: {name}, Url: {url}".format(
    name="baidu", url="www.baidu.com")
print(formatedString)

formatList = ['google', 'www.google.com']
formatedString = "Website: {0[0]}, Url: {0[1]}".format(formatList)
print(formatedString)

# Three quotation
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
print(u'Hello World!')

# Uppercase first char, lowercase others
print('Hello World!'.capitalize())

# Center the string
print(str.center(100, '*'))

