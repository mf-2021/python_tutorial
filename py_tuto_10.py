# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b, a', 'a=1; b=2').timeit())



# def average(values):
#     """数値のリストから算術平均を計算

#     print(average([20, 30, 70]))
#     """
#     return sum(values) / len(values)

# import doctest
# print(doctest.testmod())



# import unittest

# class TestStatisticalFunctions(unittest.TestCase):

#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeTrror):
#             average(20, 30, 70)

# print(unittest.main())