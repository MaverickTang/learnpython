#类
class Student(object):
    #特殊方法“__init__”前后分别有两个下划线！！！
    #__init__方法的第一个参数永远是self，表示创建的实例本身
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    # 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
    # 特殊变量是可以直接访问的，不是private变量
    
    def __init__(self, name, score):
        self.name = name
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
        # 只有内部可以访问，外部不能访问
        self.__score = score


    # 类中的所有函数都有self
    # 但是如果外部代码要获取__score怎么办？可以给Student类增加get_name和get_score这样的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.__score))
    # 封装的另一个好处是可以给Student类增加新的方法，比如get_grade
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
        
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


#类的外部调用        
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
#外部无法访问private
# print(bart.__score)
# 不能直接访问__score是因为Python解释器对外把__score变量改成了_Student__score，
# 所以，仍然可以通过_Student__score来访问__score变量：
print(bart._Student__score)
# 但不同版本的Python解释器可能会把__name改成不同的变量名

# 子类
class Animal(object):
    def run(self):
        print('Animal is running...')

# 当我们定义一个class的时候，可以从某个现有的class继承
# 新的class称为子类（Subclass）被继承的class称为基类、父类或超类（Base class、Super class）
class Dog(Animal):
#子类的run()覆盖了父类的run()
# 这样，我们就获得了继承的另一个好处：多态
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

# 子类获得了父类的全部功能
cat = Cat()
cat.run()

dog = Dog()
dog.run()

# 判断一个变量是否是某个类型可以用isinstance()判断
c=Dog()
print(isinstance(c,Dog))
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
print(isinstance(c,Animal))

#多态的好处
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
#新增一个Animal的子类，不必对run_twice()做任何修改
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
run_twice(Tortoise())

## 获取对象信息
# type
print(type('a'))
print(type(abs))
# isinstance
isinstance('a', str)
print(isinstance(b'a', bytes))

# dir方法
print(dir('a'))


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

# 紧接着，可以测试该对象的属性：
hasattr(obj, 'x') # 有属性'x'吗？
# True
obj.x
# 9
hasattr(obj, 'y') # 有属性'y'吗？
# False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
# True
getattr(obj, 'y') # 获取属性'y'
# 19
obj.y # 获取属性'y'
# 19
# 可以传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

## 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性