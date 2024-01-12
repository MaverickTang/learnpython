from collections.abc import Iterable
import os # 导入os模块，模块的概念后面讲到
## 切片
L = list(range(100))
# 第一个空格和第二个空格是区间，第三个空格是步进值
print(L[:10])
print(L[-10:])
# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
# 只写[:]就可以原样复制一个list
print(L[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

## 迭代
# python的迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# for ch in 'ABC':
#     print(ch)
# 判断str是否可迭代
print(isinstance('abc', Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

## 列表生成式
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x*x for x in range(1,11)])
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x * x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

[d for d in os.listdir('.')] # os.listdir可以列出文件和目录

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
# ['hello', 'world', 'ibm', 'apple']

# 因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else：
print([x if x % 2 == 0 else -x for x in range(1, 11)])


## 生成器
# 如果列表元素可以按照某种算法推算出来，这样就不必创建完整的list，从而节省大量的空间。这种一边循环一边计算的机制，称为生成器
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
# 可以通过next()函数获得generator的下一个返回值：
print(next(g))
# 使用for循环，因为generator也是可迭代对象：
for n in g:
    print(n)

# 第二种，在函数中将输出换为yield
# 要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib(6)
print(next(f))

# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)

# 练习
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# -*- coding: utf-8 -*-

def triangles():
    a = [1]
    b = [1,1]
    while True:
        yield a
        a = b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] +[1]
        # 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')