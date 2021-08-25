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



def this_fails():
    x = 1 / 0

try:
    this_fails
except ZeroDivisionError as err:
    print('ランタイムエラーを処理します：', err)

print(this_fails())