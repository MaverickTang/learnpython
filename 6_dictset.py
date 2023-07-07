d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Tracy')
d['Tryton']=10
# 判断在dict内的两种方法
# if d.get('Bob'):
if 'Tryton' in d:
    print(d['Tryton'])

# set自动过滤重复元素
s = set([ 2, 2,1, 1, 3, 3])
print(s)

