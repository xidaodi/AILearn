# 。os.path  系统模块中的路径模块

import os

# 将相对路径转化为绝对路径  ***
res = os.path.abspath('./')  # /Users/yc/Desktop/code

# 获取路径中的主体部分 就是返回路径中的最后一部分
res = os.path.basename('/Users/yc/Desktop/code')  # code
res = os.path.basename('/Users/yc/Desktop/code/1.py')  # 1.py

# 获取路径中的路径部分  返回路径中最后一部分之前的内容
res = os.path.dirname('/Users/yc/Desktop/code/1.py')  # /Users/yc/Desktop/code

# join()  链接多个路径，组成一个新的路径
res = os.path.join('./a/b/c/','2.jpg')  #./a/b/c/2.jpg

# split() 拆分路径，把路径拆分为路径和主体部分，
res = os.path.split('./abc/def/aaa')  # ('./abc/def', 'aaa')

# splitext() 拆分路径，可以拆分文件后缀名
res = os.path.splitext('./a/b/c/2.jpg')

# 获取文件的大小  字节数
res = os.path.getsize('./3.内置模块-数学模块-Math.py')

# 检测是否是一个文件夹,是否存在
res = os.path.isdir('/Users/yc')

# 检测文件是否存在  ***
res = os.path.isfile('./3.内置模块-数学模块-Math.py')

# exists() **** 检测路径是否存在，既可以检测文件，也可以检测路径
res = os.path.exists('/Users/yc/Desktop/code/3.内置模块-数学模块-Math.py')

#
a = '/Users/yc/Desktop/code/3.内置模块-数学模块-Math.py'
b = '/Users/yc/../yc/Desktop/code/3.内置模块-数学模块-Math.py'
# 检测两个path路径是否同时指向了一个目标位置 （两个路径必须真实）
res = os.path.samefile(a,b)
print(res)