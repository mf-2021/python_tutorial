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



def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g



class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
