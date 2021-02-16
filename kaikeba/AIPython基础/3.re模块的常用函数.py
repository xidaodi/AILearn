# re模块的常用函数

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

re.findall()

re.finditer()

re.sub()

re.split()
'''

import re
# 定义的字符串
varstr = 'iloveyou521tosimiloveda'
# 定义正则表达式
reg = 'love'

# re.findall函数,按照正则表达式的规则去字符串中进行搜索匹配所有符合规则的元素，结果返回一个列表，如果没有找到，则返回空列表
# res = re.findall(reg,varstr)


# re.finditer()函数 和findall是一样的搜索匹配规则，但是结果返回由Match对象组成的迭代器
# res = re.finditer(reg,varstr)
# for i in res:
#     print(i.group())


# re.sub() 搜索替换
'''
按照正则表达式的规则去搜索匹配要替换的字符串，完成字符串的替换
pattern 正则表达式的规则，匹配需要被替换的字符
repl：  替换后的字符
string： 原始字符串
'''
# res = re.sub(reg,'live',varstr)
# print(res)

# re.split() 按照指定的正则规则，进行数据切割
varstr = 'hello1my2name3is4chuange'
# res = re.split('\d',varstr)
# print(res)


# compile() 可以直接将正则表达式定义为 正则对象，使用正则对象直接操作

arr = [
    'i love 123 you',
    'i love 234 you',
    'i love 456 you',
    'i love 789 you',
]

reg = re.compile('\d{3}')
# reg = '\d{3}'

for i in arr:
    # res = re.search(reg,i)
    # print(res.group())
    res = reg.search(i).group()
    print(res)

