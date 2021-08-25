# s = 'Hello, world.'
# print(str(s))

# print(repr(s))

# print(str(1/7))

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)

# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# print(repr((x, y, ('spam', 'eggs'))))

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
#     print(repr(x*x*x).rjust(4))


# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# print('12'.zfill(5))

# print('-3.14'.zfill(7))

# print('3.14149265359'.zfill(5))


# print('We are the {} who say \"{}!\"'.format('knights', 'Ni'))

# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# print('This {food} is {adjective}.'.format(
#     food='spam', adjective='absolutely horrible'
# ))

# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# import math
# print('The value of PI is approximately {}.'.format(math.pi))
# print('The value of PI is approximately {!r}.'.format(math.pi))

# import math
# print('πの値はおよそ {0:.3f}である。'.format(math.pi))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#         'Dcab: {0[Dcab]:d}'.format(table))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# import math
# print('πの値はおよそ %5.3fである。' % math.pi)



# ファイルの読み書き
# f = open('test.txt', 'r')
# print(f.read())

# f = open('test.txt', 'w')
# f.write('This is a test.\n')

# value = ('the answer', 42)
# s = str(value)
# f.write(s)

# f = open('test.txt', 'rb+')
# f.write(b'0123456789abcdef')

# print(f.seek(5))
# print(f.read(1))
# print(f.seek(-3, 2))
# f.read(1)


x = [1, 'simple', 'list']
json.dumps(x)