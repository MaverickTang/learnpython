
# try...except...finally...
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
# 比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理：
# Python内置的logging模块可以非常容易地记录错误信息
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        #同样是出错，但程序打印完错误信息后会继续执行，并正常退出
        logging.exception(e)

main()


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')