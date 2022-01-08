"""
str = input("请输入:")
print("您输入的内容是:", str)
"""
import pickle
import pprint

"""
# 写入文件
f = open("/Users/Vicent/Desktop/123.txt", "w")
f.write("Python是一个非常好的语言. \n是的,的确非常好!\n")
f.close()
"""

"""
# 读文件

f = open("/Users/Vicent/Desktop/123.txt", "r")

str = f.read()
print(str)

f.close()
"""

"""
# 读一行文件

f = open("/Users/Vicent/Desktop/123.txt", "r")
str = f.readline()
print(str)
f.close()
"""

"""
# 读多行文件

f = open("/Users/Vicent/Desktop/123.txt", "r")
str = f.readlines()
print(str)
f.close()
"""

"""
# 序列化

data1 = {'a': [1, 2.0],
         'b': ('string', u'Unicode string'),
         'c': None
         }

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)

output.close()
"""

# 反序列化

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)

pprint.pprint(data1)

data2 = pickle.load(pkl_file)

pprint.pprint(data2)

pkl_file.close()