import sys

sys.path.append('../importDemo')

import support





"""
while True:
    try:
        x = int(input("请输入一个数字:"))
    except ValueError as err:
        print("你输入的不是数字,请再次尝试输入!", err)
    else:
        print("你输入的数字是:", x)
    finally:
        break
"""

"""
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
"""

"""
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)
"""
support.print_func('123')



