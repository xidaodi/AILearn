# 在当前脚本中如果需要使用一些已经定义好的功能时，可以选择对应的模块，导入后使用

# 例如使用系统模块 time
import time
print(time.time())

# 例如使用自定义异常处理 模块
import My

# 使用模块中定义的类
obj = My.MyException()
print(obj)


# 使用模块中的函数
My.func()


# 使用模块中定义的变量
print(My.love)

print(My.__name__)


# 想使用模块中的内容时，除了导入模块，还可以在在指定模块中导入指定的内容
from My import love  # 导入My模块中的love变量
from My import love as lv # 导入My模块中的love变量，起个别名
print(love)
print(lv)


