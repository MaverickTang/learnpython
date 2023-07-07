#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('包含中文的str')
ord('A')

print(ord('中')) #ord()函数获取字符的整数表示
print(chr(ord('中')))#  chr()函数把编码转换为对应的字符

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))

# 格式化字符串输出
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

s1 = 72
s2 = 85
r = (s2 - s1)/s1*100

print('%.1f%%' % r)
# format 方法，一次替代占位符{0},{1}...
# >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 'Hello, 小明, 成绩提升了 17.1%'
print('{0:.1f}%'.format(r))
# f-string 方法，使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
# >>> r = 2.5
# >>> s = 3.14 * r ** 2
# >>> print(f'The area of a circle with radius {r} is {s:.2f}')
# The area of a circle with radius 2.5 is 19.62
print(f'{r:.1f}%')
