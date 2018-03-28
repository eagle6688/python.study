a = 10
b = 10

if(a is b):
    print("a and b with same object")
else:
    print("a and b with different object")

b = 20

if(a is not b):
    print("a and b with different object")
else:
    print("a and b with same object")
