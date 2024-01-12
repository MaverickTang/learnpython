# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
import pdb

def foo(s):
    n = int(s)
    #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
    # 启动Python解释器时可以用-O参数来关闭assert：
    # $ python -O err.py
    pdb.set_trace() # 运行到这里会自动暂停
    # python -m pdb err.py
    # 输入命令l来查看代码
    # 输入命令n可以单步执行代码
    # 任何时候都可以输入命令p 变量名来查看变量
    # 输入命令q结束调试，退出程序
    assert n!=0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()