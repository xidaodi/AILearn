# 序列化-pickle

import pickle

'''
什么是序列化？为什么需要序列化？
1。序列化是指可以把python中的数据，以文本或二进制的方式进行转换，并且还能反序列化为原来的数据
2。一般来说数据在程序与网络中进行传输和存储时，需要以更加方便的形式进行操作，因此需要对数据进行序列化

pickle模块提供的函数
    dumps() 序列化，返回一个序列化后的二进制数据 可以把一个python的任意对象序列化成为一个二进制
        pickle.dumps(var)
    loads() 反序列化，返回一个反序列化后的python对象  可以把一个序列化后的二进制数据反序列化为python的对象
        pickle.dumps(var)

    dump() 序列化，把一个数据对象进行序列化并写入到文件中
        参数1，需要序列化的数据对象
        参数2，写入的文件对象
        pickle.dump(var,fp)
    load() 发序列化，在一个文件中读取序列化的数据，并且完成一个反序列化
        参数1，读取的文件对象
        pickle.load(fp)
    
'''


# 1。基本的序列化与反序列化操作
vars = 'i love you'  # b'\x80\x03X\n\x00\x00\x00i love youq\x00.' <class 'bytes'>
vars = [1,2,3,4]  #b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04e.' <class 'bytes'>
vars = {'name':'张三','age':20,'sex':'m'} # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00\xe5\xbc\xa0\xe4\xb8\x89q\x02X\x03\x00\x00\x00ageq\x03K\x14X\x03\x00\x00\x00sexq\x04X\x01\x00\x00\x00mq\x05u.' <class 'bytes'>

# 使用 pickle.dumps方法进行序列化成为一个二进制的数据
res = pickle.dumps(vars)

# 使用 loads方法完成一个反序列化
res = pickle.loads(res) # {'name': '张三', 'age': 20, 'sex': 'm'} <class 'dict'>

# print(res,type(res))


# 如何把一个python数据进行序列化后写入文件？并且再次读取出来？
# 2。 使用 dumps loads 方法完成
# 定义数据
# vars = {'name':'张三','age':20,'sex':'m'}
# # 进行序列化
# res = pickle.dumps(vars)
# # 写入文件
# with open('./data.txt','wb') as fp:
#     fp.write(res)

# 如何把一个反序列的二进制文件读取处理，并完成反序列化
# 打开文件进行读取
# with open('./data.txt','rb') as fp:
#     res = fp.read()
# # 进行反序列化
# vardict = pickle.loads(res)
# print(vardict)

# 使用 pickle模块给提供的方法完成 load，dump
# 写
# vars = {'name':'张三','age':20,'sex':'m'}
# with open('./data2.txt','wb') as fp:
#     # 在此处调用pickle模块的方法
#     pickle.dump(vars,fp)

# 读
# with open('./data2.txt','rb') as fp:
#     # 在此处调用pickle模块的方法
#     newdict = pickle.load(fp)
# print(newdict)







