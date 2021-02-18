# 什么是异常

'''
什么是异常？

异常简单理解，就是非正常，没有达到预期目标。
异常是一个事件，并且这个异常事件在我们程序员的运行过程中出现，会影响我们程序正常执行。

异常分两种：
    1. 语法错误导致的异常
    2. 逻辑错误导致的异常

在程序无法正常运行处理时，就会出现一个异常，在python中异常是一个对象，表示一个错误。
例如：获取一个不存在的索引

Traceback (most recent call last):
  File "/Users/yc/Desktop/code/1.异常处理-什么是异常？.py", line 12, in <module>
    print(varlist[3])
IndexError: list index out of range


IndexError  异常类
list index out of range  异常信息

'''
# varlist = [1,2,3]
# print(varlist[2])


'''
如何处理异常？

1. 如果错误发生的情况是可以预知的，那么就可以使用流程控制进行预防处理
    比如： 两个数字的运算，其中一个不是数字，运算就会出错。这时可以去判断来预防
'''
n2 = 3
if isinstance(n2,int):
    res = 10+n2
    print(res)

'''
2. 如果错误的发生条件不可预知，就可以使用 try。。。except。。 在错误发生时进行处理
语法：
try:
    可能发生异常错误的代码
except:
    如果发生异常则进入 except 代码块进行处理
'''

# 假设读取的文件不存在，会发生错误，可以使用两种方式进行处理，
# 1。可以在文件读取前先判断当前的文件是否存在
# 2。也可以使用try 。。。 except。。在错误发生时进行处理
# 注意：try。。except。。是在错误发生后进行的处理。和if有着根本性的区别。
try:
    with open('./user.txt','r') as fp:
        res = fp.read()
    print(res)
except:
    print('文件不存在')

print('程序的继续执行。。。')

