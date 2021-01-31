# 序列化 json
'''
什么是json？
JSON (JavaScript Object Notation)
JSON 是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式。
JSON 在js语言中是一个对象的表示方法，和Python中的字典的定义规则和语法都很像
JSON 在互联网中又是一种通用的数据交换，数据传输，数据定义的一种数据格式

python中提供的json模块，可以把一些符合转换的python数据对象，转为json格式的数据
    json.dumps()
    json.loads()

    json.dump()
    json.load()

'''

import json
# 以下语法格式定义的是一个 字典 数据类型

vardict = {'name':'admin','age':20,'sex':'男'}
vardict = [1,2,3]
vardict = [{'name':'admin','age':20,'sex':'男'},{'name':'aa','age':21,'sex':'m'}]

vardict = 'abcdef'  # 只是转为了字符串而已，
vardict = 521       # 只是转为了数字而且

# print(vardict,type(vardict))

# 使用 json模块的 dumps方法进行 json格式的转换
res = json.dumps(vardict)
# print(res,type(res))

# 使用 loads方法进行反转换
res = json.loads(res)
# print(res,type(res))


# dump  load
# 写
vardict = [{'name':'admin','age':20,'sex':'男'},{'name':'aa','age':21,'sex':'m'}]
# with open('./data.json','w') as fp:
#     json.dump(vardict,fp)

# 读
with open('./data.json','r') as fp:
    new = json.load(fp)
print(new)




