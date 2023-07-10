#变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

## 返回函数
# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f=lazy_sum(1,3,5,7)
print(f())

## 闭包
# 返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

fx = count()
for f in fx:
    print(f())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):# 再创建一个函数，用该函数的参数绑定循环变量当前的值
        def g():# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

fx = count()
for f in fx:
    print(f())

## nonlocal方法
def inc():
    x = 0
    def fn():
        nonlocal x
        #x作为局部变量并没有初始化，直接计算x+1是不行的。
        #但我们其实是想引用inc()函数内部的x，所以需要在fn()函数内部加一个nonlocal x的声明
        # 加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

def createCounter():
    n=0
    def counter():
        nonlocal n
        n=n+1
        return n
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 匿名函数
# 匿名函数一定有lambda，没有return，但只能由一个简单表达式组成
f = lambda x: x * x
print(f(5))
is_odd = lambda x: x%2==1
L = list(filter(is_odd, range(1, 20)))
print(L)

# 装饰器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 我们要借助Python的@语法，把decorator置于函数的定义处
# 相当于执行了语句：now = log(now)
@log
def now():
    print('2023-7-8')
# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字：
now.__name__
now()

# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')#等效于now = log('execute')(now)
def now():
    print('2015-3-25')
now()
print(now.__name__)
# log因为嵌套wrapper，将函数名字改变了
def log(func):
    @functools.wraps(func)# 解决函数名字改变的问题
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

## 偏函数
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个更简单的新函数
int2=functools.partial(int,base=2)
print(int2('100000'))



