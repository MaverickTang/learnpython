import math

# 函数可以传多个值，本质是数组
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    
# 函数可以不传值
def nop():
    pass

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#关键字参数 ** 可以不传，也可以传入任意个数的关键字参数，接收的是一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 可变参数 * ，可以传任意个参数进来，然后组成数组输入，甚至可以传0个，接收的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# 尾递归优化
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(power(5))
print(calc(1,5,2))
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))
person('tht',19,gender='M', Looks='Headsome')

