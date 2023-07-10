#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
# 以上就是Python模块的标准文件模板

' a test module '

__author__ = 'Haotian Tang'

import sys

#正常的函数和变量名是公开的（public），可以被直接引用
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，
# 比如__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问
# 我们自己的变量一般不要用这种变量名
if __name__=='__main__':
    test()

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该（注意不是不能）被直接引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)