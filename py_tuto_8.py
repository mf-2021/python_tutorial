# # while true print('Hello world')

# # print(10 * (1/0))

# # 4 + spam*3

# '2' + 2

# import sys

# try:
#     f = open('test.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("データが整数に変換できません。")
# except:
#     print("予期せぬエラー：", sys.exc_info()[0])
#     raise


# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('Cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close



# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)

#     x, y = inst.args
#     print('x=', x)
#     print('y=', y)



# def this_fails():
#     x = 1 / 0

# try:
#     this_fails
# except ZeroDivisionError as err:
#     print('ランタイムエラーを処理します：', err)

# print(this_fails())



# raise NameError('Hi There')



# try:
#     raise NameError('HiThere')
# except NameError:
#     print('例外が飛んでった！')
#     raise



# class MyError(Exception):
#     def __int__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occured, value:', e.value)



class Error(Exception):
    """このモジュールの例外のベースクラス"""
    pass

class InputError(Error):
    """入力エラーで送出される例外
    
    属性：
        expression -- エラーが起きた入力式
        message -- エラーの説明
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """許可されない状態繊維を起こそうとする操作があれば送出される
    
    属性：
        previous -- 遷移前の状態
        next -- 移ろうとした状態
        message -- その遷移がなぜ許可されないかの説明
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

