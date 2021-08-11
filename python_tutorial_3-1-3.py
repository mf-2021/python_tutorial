squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])

print(squares[:])
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(cubes)
print(4 ** 3)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# フィボナッチ級数
# 2項の和により次項が定まる
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

i = 256 * 256
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b