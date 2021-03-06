# 5.1　リストについての補足
# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))

# a.insert(2, -1)
# a.append(333)
# print(a)

# print(a.index(333))

# a.remove(333)
# print(a)

# a.reverse()
# print(a)

# a.sort()
# print(a)

# a.pop()
# print(a)



# 5.1.1 リストをスタックとして使う
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)

# print(stack.pop())
# print(stack)

# print(stack.pop())

# print(stack.pop())
# print(stack)



# 5.1.2 リストをキューとして使う
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# print(queue)
# queue.append("Graham")
# print(queue.popleft())
# print(queue.popleft())
# print(queue)



# 5.1.3 リスト内包
# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)

# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)


# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec])

# print([x for x in vec if x >= 0])

# print([abs(x) for x in vec])


# freshfruit = [' banana ', ' loganberry ', 'passion fruit ']
# print([weapon.strip() for weapon in freshfruit])

# print([(x, x**2) for x in range(6)])

# # print(x, x**2 for x in range(6))

# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for elem in vec for num in elem])

# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])



# 5.1.4 入れ子のリスト内包
# matrix = [
#     [1, 2, 3, 4], 
#     [5, 6, 7, 8], 
#     [9, 10, 11, 12]
# ]

# print([[row[i] for row in matrix] for i in range(4)])

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)


# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# print(list(zip(*matrix)))



# del文
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)

# del a[2:4]
# print(a)

# del a[:]
# print(a)

# del a
# print(a)



# 5.3　タブルとシーケンス
# t = 12345, 54321, 'hello!'
# print(t[0])
# print(t)

# u = t, (1, 2, 3, 4, 5)
# print(u)

# # t[0] = 88888

# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# empty = ()
# singleton = 'hello',
# print(len(empty))

# print(len(singleton))

# print(singleton)



# 集合（set）
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)

# print('orange' in basket)

# print('crabgrass' in basket)


# a = set('abracadabra')
# b = set('alacazam')
# print(a)

# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)



# 5.5 ディクショナリ
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)

# print(tel['jack'])

# del tel['sape']
# tel['irv'] = 4127
# print(tel)

# print(list(tel.keys()))

# print(sorted(tel.keys()))

# print('guido' in tel)

# print('jack' not in tel)

# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# print({x: x**2 for x in (2, 4, 6)})

# print(dict(sape=4139, guido=4127, jack=4098))



# 5.6　ループのテクニック
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for f in sorted(set(basket)):
    print(f)


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)