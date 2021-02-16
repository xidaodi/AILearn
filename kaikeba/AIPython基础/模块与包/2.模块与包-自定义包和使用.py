# 如果需要使用包可以直接导入包

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


# 导入方式的分类 绝对导入，相对导入
