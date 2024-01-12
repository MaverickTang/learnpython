import sys
import hello

sys.path.append('/Users/mt/my_py_scripts')
# 在同一级文件夹，通过import导入自己编写的模块
hello.test()
print(hello.greeting("Maverick"))

