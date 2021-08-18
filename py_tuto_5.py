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
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())

print(stack.pop())
print(stack)