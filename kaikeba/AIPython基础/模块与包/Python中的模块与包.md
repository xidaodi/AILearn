### Python中的模块与包

## 模块

> 定义的一个python的文件，后缀名为.py。这个文件被称为模块。
>
> 模块中通常会定义一些相似的 类，函数等代码内容，提供给别的程序引入后使用。

#### 系统模块

> 系统模块就是一个python的程序脚本，专门提供给我们自己的程序使用。它们是在安装好python环境时，就已经存在的，需要的时候可以使用 import 导入到程序中使用。
>
> import logging，json，time。。。。

#### 自定义模块

> 就是自己创建一个python脚本，定义一些类或方法，供别的脚本导入后使用。

例如定义一个My.py的文件如下

```python
# My.py

# 定义类
class MyException():
    pass

# 定义函数
def func():
    print('我是一个模块中的func函数')
    
# 定义变量
love = 'iloveyou'
```

在定义一个python脚本就可以引入上面的文件作为模块使用

main.py

```python
# main.py 在当前脚本中如果需要使用一些已经定义好的功能时，可以选择对应的模块，导入后使用

# 使用系统模块 time
import time
print(time.time())

# 使用自定义异常处理 模块
import My

# 使用模块中定义的类
obj = My.MyException()
print(obj)

# 使用模块中的函数
My.func()

# 使用模块中定义的变量
print(My.love)

# 想使用模块中的内容时，除了导入模块，还可以在在指定模块中导入指定的内容
from My import love  # 导入My模块中的love变量
from My import love as lv # 导入My模块中的love变量，起个别名
print(love)
print(lv)
```

#### 模块中的测试代码

```python
# 自定义模块中，通常只是去定义类或函数，变量，等，并不调用
# 如果在自定义模块中，想要写一些测试代码，在当前模块作为主程序使用时执行，
# 而作为模块被别的程序导入时不执行，那么可以把测试代码写到 下面代码块中
if __name__ == '__main__':
    print('这个位置写的代码只有当前脚本被直接运行时触发')
    
# 特殊的变量 __name__
# __name__ 这个变量，在当前脚本作为模块被别的程序导入是 __name__的值 是当前这个模块的名称
#在当前脚本被作为主程序直接由python解析运行时，__name__的值 是 '__main__'
name = __name__
print(name)
```

## 包

> 包可以理解为是一个文件夹，里面包含了多个python文件。

### 包的结构：

```python
'''
package/   # 包(文件夹)
├── __init__.py  # 包中的初始化文件
├── a.py         # 包中的模块
├── b.py
└── ps/   # 子包
  ├── __init__.py
  ├── c.py
  └── d.py
'''
```

### 包的使用方法

```python
# 1. 直接把包当作模块导入，可以用的内容是 __init__.py文件中定义的
# 不推荐这种用法
import package
package.funcpa()

#2。 可以导入模块中的所有内容
# 注意这个内容是由 __init__.py文件中定义的 __all__ 这个变量指定的模块
# 好处是可以直接导入指定的所以模块，并且使用时，直接使用指定的模块名即可
from package import  *
a.funca()
b.funcb()

# 3。 导入指定包中的指定模块
from package import a
a.funca()

# 4。从指定包的指定模块中导入指定的内容
from package.b import funcb
funcb()

# 5。从指定包的子包中导入模块
from package.ps import c
c.funcc()

# 6。 从指定包的子包的指定模块中导入指定内容
from package.ps.d import funcd
funcd()
```

## 导入方式的分类

### 绝对导入

```
# 绝对导入的方式会使用[搜索路径]去查找和导入指定的包或模块
import 模块
import 包
import 包.模块
from 模块 import 内容
from 包 import 模块
from 包.模块 import 内容
```

### 相对导入

**注意：相对导入只能在非主程序的模块中使用，不需要直接运行的模块文件**

```
# 相对导入 
from .包名/模块名 import 模块/内容
from ..包名/模块名 import 模块/内容

. 代表当前
..代表上一级
```

### 搜索路径

> 在导入模块或包时，程序查找的路径

```python
'''
主要的搜索路径
1. 当前导入模块的程序所在的文件
2. python的扩展目录中 C:/Users/username/AppData/local/.../Python37/lib
3. python解释器指定的其它 第三方模块位置 /lib/sitepackages
'''
# 在当前脚本中查看 包或模块 的 搜索路径
import sys
print(sys.path)
'''
[   
    '', 
    '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', 
    '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', 
    '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
    '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages'
 ]
'''

# 可以自己定义一个路径，加入到搜索路径中
sys.path.append('/Users/yc/Desktop')
```

## 单入口程序

> 单入口程序是指整个程序都是经过一个主程序文件在运行，其它程序都封装成了包或模块

```python
# 单入口文件是作为程序直接被运行的唯一文件，其它都是作为模块或包，被导入单入口中去执行
'''
ATM/
|---- main.py  # 当前程序的主入口文件，单入口文件,唯一直接运行的文件
|---- package/ # 主要程序模块包
|---- |----- __init__.py  # 包的初始化文件
|---- |----- View.py      # 视图函数模块
|---- |----- Controller.py# 控制器模块
|---- |----- Card.py      # 银行卡模块
|---- |----- User.py      # 用户模块
|---- databases/ # 数据存储文件夹
|---- |---- user.txt
|---- |---- user_id_card.txt

main是程序的主入口文件，会被直接作为主程序运行，所以main.py文件中必须使用 绝对导入 方式
'''
```