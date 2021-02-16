# re正则模块的相关函数

'''
re.match() 函数
    从头开始匹配，如果第一个就符合要求，那么匹配成功，
    如果第一个不符合规则，返回None
    匹配成功后返回Match对象，
    成功后可以使用group()和span()方法获取数据和下标区间

re.search() 函数
    从字符串的开头开始进行搜索式的匹配
    匹配成功则返回Match对象，匹配失败则返回None
    成功后可以使用group()和span()方法获取数据和下标区间

search和match方法的区别？
'''

import re

# 定义的字符串
varstr = 'iloveyou521tosimiloveda'

# 定义正则表达式
reg = 'lovel'

# 使用match函数
# res = re.match(reg,varstr)
# print(res)          # 成功返回Match对象，失败返回None
# print(res.group())  # 获取匹配的数据
# print(res.span())   # 获取匹配的数据的下标区间

# 使用search函数
res = re.search(reg,varstr)
print(res)
print(res.group())
print(res.span())
