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

#     x = MyClass()

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

