## 文件读取
try:
    f = open('/Users/mt/Desktop/PROGRAM/Basics/Python/learnpython/README.md', 'r')
    print(f.read())
finally:
    if f:
        #最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭
        # 因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限
        f.close()

# 自动调用close方法，也可以用相对路径
with open('README.md', 'r') as f:
    print(f.read())

# 以`'w'`模式写入文件时，如果文件已存在，会直接覆盖
# 可以传入`'a'`以追加（append）模式写入
f = open('test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('test.txt', 'w') as f:
    f.write('Hello, world!')



## StringIO and ByteIO

#StringIO顾名思义就是在内存中读写str
# write
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#read
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f.read())

import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数
print(os.name)

# 要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ)

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
print(os.path.join('/Users/mt', 'testdir'))

# 然后创建一个目录:
os.mkdir('/Users/mt/testdir')
# 删掉一个目录:
os.rmdir('/Users/mt/testdir')
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')


# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
# pickle.dumps()方法把任意对象序列化成一个bytes
# 可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open('dump.txt', 'rb')
print(pickle.load(f))
f.close()
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
json.dumps(d)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s))#dump传入参数需要转化



