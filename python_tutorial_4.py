# x = int(input("整数を入れてください："))

# if x < 0:
#     x = 0
#     print('負数はゼロとする')
# elif x == 0:
#     print('ゼロ')
# elif x == 1:
#     print('ひとつ')
# else:
#     print('もっと')

# 4.2　for文
# words = ['cat', 'window', 'defenstrate']
# for w in words:
#     print(w, len(w))

# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0, w)

# print(words)

# 4.3 range() 関数
# for i in range(5):
#     print(i)
    

# for i in range(5, 10):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# print(len(a))
# for i in range(len(a)):
#     print(i, a[i])

# print(range(10))

# print(list(range(5)))


# 4.4 break文とcontinue文、ループにおけるelse節
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)


# 4.5 pass文
# while True:
#     pass


# ４.6 関数の定義
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# fib(4000)

# print(fib)
# f = fib
# f(100)

# print(fib(0))


# def fib2(n):
#     """nまでのフィボナッチ級数からなるリストを返す"""
#     result = []
#     a, b = 0, 1

#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return result

# f100 = fib2(100)
# print(f100)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('非協力的ユーザー')
        print(complaint)


# ask_ok('Do you really want to quit?')

# ask_ok('OK to overwrite the file?', 2)

# ask_ok('OK to overwrite the file?', 2, 'come on, only yes or no!')


# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1, [5]))
print(f(2))
print(f(3))