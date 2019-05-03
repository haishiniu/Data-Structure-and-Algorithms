# -*- coding: utf-8 -*-
# !/usr/bin/python


def digui(num):
    print(num)
    if num > 0:
        num_number = num - 1
        digui(num_number)
    else:
        print('<---->')
    print(num)

digui(3)

# 整个迭代过程
# digui(3):
#     print(3)
#     if 3 > 0:
#         digui(2):
#             print(2)
#             if 2 > 0:
#                 digui(1):
#                     print(1)
#                     if 1 > 0:
#                         digui(0):
#                             print(0):
#                             if 0 > 0:
#                                 digui(-1):
#                             else:
#                                 print('<--->')
#                             print(0)
#                     print(1)
#             print(2)
#     print(3)
#
