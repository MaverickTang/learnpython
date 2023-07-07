## list
classmates = ['Michael', 'Bob', 'Tracy']
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
classmates[0]
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
classmates[-1]
# 'Tracy'
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
# 可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
# list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
# list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
## tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 要定义一个只有1个元素的tuple，如果你这么定义：
t = (1,)
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：