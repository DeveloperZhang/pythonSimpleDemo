"""
def max_fuc(a, b):
    if a > b:
        return a
    else:
        return b


a1 = 4
b1 = 5
print(max_fuc(a1, b1))
"""

"""
def change_value(a):
    print(id(a))
    a = 10
    print(id(a))


aInput = 1
print(f"{id(aInput)}:{aInput}")
change_value(aInput)
print(f"{id(aInput)}:{aInput}")
"""

"""
# 引用传参


def change_reference(my_list):
    print(id(my_list))
    my_list.append(100)
    print(id(my_list))


listInput = [10, 20, 30]
print(f"{id(listInput)}:{listInput}")
change_reference(listInput)
print(f"{id(listInput)}:{listInput}")
"""

"""
def print_info(arg1, *var_tuple):
    print("输出:")
    print(arg1)
    for var in var_tuple:
        print(var)
    return


print_info(10)
print_info(10, 20, 30)
"""

"""
# 匿名函数

my_sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为:", my_sum(10, 20))
print("相加后的值为:", my_sum(20, 20))
"""


