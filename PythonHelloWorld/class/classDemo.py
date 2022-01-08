"""
class MyClass:
    i = 12345
    def f(self):
        return "hello world"

x = MyClass()
print("MyClass 类的属性 i 为:", x.i)
print("MyClass 类的方法 f 输出为:", x.f())
"""

class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, -4.5)
print(x.r, x.i)