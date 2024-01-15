# -*- coding: utf-8 -*-
"""
file：
mode:
encoding:
文件名，需要操作的文件
操作模式
w write 51
r read 读取
a append 追加
编码格式 主流有两种utf-8（万国码 主流的）
gbk（主要是在windows 下运行）
utf-8-sig 兼容性的编码，在windows 下面不会显示乱码
"""
## 写入
# Mode有 r 只读 w 只写 a 追加 + 读写
# 打开一个文件
file = open(file='文件名.txt', mode='w',encoding='utf-8')
# 往文件里面写入数据
file.write( 'hello world !')
# 关闭一个文件
file.close()
## 读取
 # with 关键字上下文管理器当不再with语句里面的时候，会自动关闭文件
# as 重命名起别名 file，使用file指代 open 打开的文件
# file = open(file='hello.txt', mode='r', encoding='utf-8')
# open(file= 'hello. txt', mode='r', encoding='utf-8')
with open(file='文件名.txt', mode='r', encoding='utf-8') as file:
    line = file. readline()
    # 读取一行
    print (line)
    lines = file.readlines()
    # 读取很多行，是一个列表
    print (lines)