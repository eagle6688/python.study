import time

# time
print('\n')
print('Time'.center(50, '*'))

timestamp = time.time()
print('The current timestamp: ', timestamp)

# ctime
print('\n')
print('ctime'.center(50, '*'))
print(time.ctime(timestamp))

# gmtime
print('\n')
print('gmtime'.center(50, '*'))
print(time.gmtime(timestamp))

# localtime
print('\n')
print('localtime'.center(50, '*'))

localtime = time.localtime(timestamp)
print('The local time: ', localtime)

# asctime
print('\n')
print('asctime'.center(50, '*'))

localtime = time.asctime(localtime)
print('The local time: ', localtime)

# strftime
print('\n')
print('strftime'.center(50, '*'))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# clock
print('\n')
print('clock'.center(50, '*'))


def procedure():
    time.sleep(2.5)


t0 = time.clock()
procedure()
print(time.clock() - t0)

# mktime
print('\n')
print('mktime'.center(50, '*'))

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print("time.mktime(t) : %f" % secs)

# timezone
print('\n')
print('timezone'.center(50, '*'))
print(time.timezone)

# altzone
print('\n')
print('altzone'.center(50, '*'))
print(time.altzone)
