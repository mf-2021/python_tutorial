# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlacal spam"
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("Afrer nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope;", spam)



# class MyClass:
#     """A simple example class"""
#     i = 12345
#     def f(self):
#         return 'hello world'

#     def __init__(self):
#         self.data = []

# x = MyClass()
# print(x.i)



#     x.counter = 1
#     while x.counter < 10:
#         x.counter = x.counter * 2
#     print(x.counter)
#     del x.counter


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(x.r, x.i)


# xf = x.f
# while True:
#     print(xf())



# class Dog:
    
#     kind = 'canine'

#     def __init__(self, name):
#         self.name = name

# # インスタンス作成
# d = Dog('Fibo')
# e = Dog('Buddy')

# print(d.kind)
# print(e.kind)
# print(d.name)
# print(e.name)



# class Dog:

#     tricks = []

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# # インスタンス化
# d = Dog('Fibo')
# e = Dog('Buddy')

# print(d.add_trick('ころがる'))
# print(e.add_trick('死んだふり'))
# print(d.tricks)


# class Dog:

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# # インスタンス化
# d = Dog('Fibo')
# e = Dog('Buddy')

# d.add_trick('ころがる')
# e.add_trick('死んだふり')

# print(d.tricks)
# print(e.tricks)



# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1
#     def g(self):
#         return 'hello world'
#     h = g



# class Bag:
#     def __init__(self):
#         self.data = []
#     def add(self, x):
#         self.data.append(x)
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)



# class base():
#     def a(self):
#         print('私の名前はbase.aです。base.bをコールします。')
#         self.b()
#     def b(self):
#         print('私の名前はbase.bです。der.bでオーバーライドされます')

# class der(base):
#     def b(self):
#         print('ウヒョ！オイラはder.bだよ。')

# b = base()
# d = der()
# print(b.a())
# print(d.a())



# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.items_list.append(item)



# class Employee:
#     pass

# john = Employee()

# john.name = 'John Doe'
# john.dept = 'computer lab'
# john.salary = 1000



# class B(Exception):
#     pass
# class C(B):
#     pass
# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")



# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one': 1, 'two': 2}:
#     print(key)
# for char in "123":
#     print(char)
# for line in open("test.txt"):
    # print(line, end=" ")



# s = 'abc'
# it = iter(s)
# print(it)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



# class Reverse:
#     "シーケンスを逆順にループする反復子"
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# rev = Reverse('spam')
# print(iter(rev))

# for char in rev:
#     print(char)



# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]

# for char in reverse('golf'):
#     print(char)



# print(sum(i*i for i in range(10)))

# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# print(sum(x*y for x, y in zip(xvec, yvec)))

# from math import pi, sin
# sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
# print(sine_table)

# unique_words = set(word  for line in page  for word in line.split())
# print(unique_words)

# valedictorian = max((student.gpa, student.name) for student in graduates)
# print(valedictorian)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))