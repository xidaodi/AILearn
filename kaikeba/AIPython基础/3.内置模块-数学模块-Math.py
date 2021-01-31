# 数学模块 Math

import math
# math的相关函数。一部分
# math.ceil()  向上取整,内置函数 round() 四舍五入
res = math.ceil(2.55)

# math.floor() 向下取整，
res = math.floor(2.55)

# math.pow() 计算数值的n次方,结果是浮点
res = math.pow(2,3)

# math.sqrt() 开平方运算，结果是浮点
res = math.sqrt(12)

# math.fabs() 计算绝对值,结果是浮点
res = math.fabs(-3.14)

# math.modf() 把一个数值拆分成小数和整数组成的元组
res = math.modf(3)  #(0.0, 3.0)

# math.copysign(x,y)  把第二个参数的正负符合拷贝给第一个参数,结果为浮点数
res = math.copysign(-3,99)

# math.fsum() 将一个容器类型数据中的元素进行一个求和运算，结果为浮点数
# res = math.fsum('123')  # X TypeError: must be real number, not str
# res = math.fsum({1,2,3}) # 注意：容器中的元素必须是可以运算的number类型

# math.factorial(x)  以一个整数返回 x 的阶乘
res = math.factorial(10)  #

# 常量
# 数学常数 π = 3.141592...，精确到可用精度。
res = math.pi
# print(res)

print('hello 你瞅啥?')

