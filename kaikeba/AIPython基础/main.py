# var1="123"
# var2=["a","b","c"]
# var3=("A","B","C")
# var4={"1","2","3"}
# res=zip(var1,var2,var2,var4)
# res=list(res)
# print(res)
# x,y,z,h=zip(*res)
# print(x,y,z,h)


# a=100.034
# b="奔流"
# c="君不见"
# vara = '{c}，{a:.2f}之水天上来，{b}到海不复回.'.format(a=a,b=b,c=c)
# print(vara)

# var="I love you"
# res=var.capitalize()
# res2=var.title()
# print(res,res2)
# res3=var.startswith("l",2)
# print(res3)


# vars="hellothisisruijunlovesplace"
# res=vars.find("love")
# res=vars.count("l")
# print(res)

# var="i_love_you"
# res=var.split("_",1)
# print(res)
#
# arr=['i','love','you']
# res="_".join(arr)
# print(res)
#
# arr="  ilovebaby  "
# res=arr.strip(" ")  #去除两侧的指定字符
# print(res)
# ary=res.replace("baby","tong")
# print(ary)
#
# res=ary.center(2,"*")
# print(res)



# lis1=["hi","this",[1,2,3,4]]
# newlist=lis1.copy()
# print(newlist)
# del lis1[2][2]
# print(newlist,id(newlist[2]))
# print(lis1,id(lis1[2]))     #多维列表的浅拷贝



# import copy
# lis1=["hi","this",[1,2,3,4]]
# newlist=copy.deepcopy(lis1)  #深拷贝
# print(newlist)
# del lis1[2][2]
# print(newlist,id(newlist[2]))
# print(lis1,id(lis1[2]))



# list=[i**2 for i in range(10) if i%2==0]
# print(list)
# str="1234"
# lis=[int(i)**2 for i in str]
# print(lis)


# list=[(x,y) for x in [1,2,3] for y in [4,5,6] if x!=y]
# print(list)
# lis=[f"{x}*{y}={x*y}" for x in range(10) for y in range(10)]
# print(lis)



# def hello():      # 生成器函数，返回一个迭代器
#     print("hello 1")
#     yield 1
#     print("hello 2")
#     yield 2
# res=hello()
# print(list(res))



# def feibo():
#     a,b,i=0,1,0
#     print(a,b,i)
#     while i<4:
#         yield b
#         a,b=b,a+b
#         i+=1
# res=feibo()
# print(list(res))


# dict=dict(name="hello",age=10,sex="M")
# print(dict)
# dict["name"]="hi"
# print(dict)
# res="M" in dict
# print(res)
# res=dict.keys()
# print(res)
# for k,v in dict.items():
#     print(f"{k}-{v}")
# dict.update(score=100)
# print(dict)
# newdict={ v:k for k,v in dict.items() if int(v)%2==0}
# print(newdict)


# print("hello",end=",")
# print("world")


# vars={1,2,3,"hello",0, False,(1,2,3)}
# print(vars,len(vars))
# vars.add("123")
# print(vars)
# vars.pop()
# print(vars)
# vars.remove("hello")
# print(vars)
# vars.update("hello")
# print(vars)
# res=vars.copy()
# print(res)
# v=frozenset((1,2,3))
# print(v)
# vars.add(v)
# print(vars)
# var1={1,2,3}
# var2={2,3,4}
# newvar={i+j for i in var1 for j in var2 if i%2==0}
# print(newvar)
# res=var1 & var2        #交集
# print(res)
# res=var1 | var2       #并集
# print(res)
# res=var1-var2           #差集
# print(res)
# res=var1^var2         #对称差集
# print(res)
# res=var1.intersection(var2)     #是否有交集
# print(res)
# res=var1.intersection_update(var2)           #       是否有交集 ，然后更新到var中
# print(res,var1)
# res=var1.union(var2)               #并集
# print(res)
# res=var1.difference(var2)          #差集
# print(res)
# res=var1.symmetric_difference(var2)     #对称差集
# print(res)
# print(var1,var2)
# res=var2.issubset(var2)            #是否为超集
# print(res)
# res=var1.isdisjoint(var2)           #是否没有交集
# print(res)

# fp=open(r"1.txt","r",encoding="utf-8")
# res=fp.read()
# print(res)
# fp.close()


# var="i love you"
# var=[1,2]
# var=["i","love","you","11"]
# var={"name":"ruchan","age":"13"}  #只能写入Key值
# with open(r"1.txt","w",encoding="utf-8") as fp:
#     # fp.write(var)  #只能写入字符串
#     fp.writelines(var)
#     # fp.seek(0)  #移动光标的位置，移动字节的位置
#     # res=fp.read()
#     # print(res)


# with open(r"1.txt","r",encoding="utf-8") as fp:
#     fp.seek(0) # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
#     res=fp.read(4)
#     res0=fp.readline(3) #  3指的是字节数
#     res00=fp.readlines() # ['疑似地上霜\n', '孤舟蓑笠翁\n', '独钓寒江雪'],()里也可以填字节数
# print(res)
# print(res00)

# with open(r"1.txt","r+",encoding="utf-8") as fp:
#     res=fp.truncate(2) #从当前光标位置，截取保留2个字节
#     print(res)


'''
注册/登录练习
'''
# username=[]
# password=[]
#
# def read_user_info():
#     with open(r"1.txt","a+",encoding="utf-8") as fp:
#
#         fp.seek(0)
#         res=fp.readlines()
#         print(res)
#         for i in res:
#             r=i.strip("\n")
#             s=r.split(":")
#             print(s)
#             username.append(s[0])
#             password.append(s[1])
#
#     print(username)
#     print(password)
#
#
# def Registration():
#     user_name_input=input("Welcome registration, please input your username: ")
#     while user_name_input in username:
#         user_name_input=input("the username has exited! please input again:")
#
#     user_name=user_name_input
#
#
#     paswrd_is_right=True
#
#     while paswrd_is_right:
#         pass_word1=input("please input your password: ")
#         pass_word2=input("please confirm your password: ")
#         if pass_word1!=pass_word2:
#             print("the passwords you input are not the same, please input them again")
#         else:
#             paswrd_is_right=False
#     pass_word=pass_word2
#     with open(r"1.txt","a+",encoding="utf-8") as fp:
#         fp.write(f"{user_name}:{pass_word}\n")
#     print("Congratulations, you have registered successfully!")
#     print(user_name,"\t",pass_word)
#
#
# def SignIn():
#
#     user_name_signin=input("please input your username: ")
#     while user_name_signin not in username:
#         user_name_signin=input("the username does not exist, please input again: ")
#
#     i=username.index(user_name_signin)
#     print(i,password[i])
#     pass_word_signin=input("please input your password: ")
#     count=0
#     while pass_word_signin!=password[i]:
#
#         pass_word_signin=input("the password is uncorrect, please input your password again: ")
#         count+=1
#         if count==3:
#             print("your account has been locked as your input wrong password for three times!")
#             break
#
#     print("Congratulations, you have signed in successfully!")
#
#
# if __name__ == '__main__':
#
#     while True:
#         read_user_info()
#         print("\nwelcome to Kaikeba, please choose your fuction:")
#         print("0 Registration")
#         print("1 SignIn")
#         func=int(input())
#         if func==0:
#             Registration()
#
#         elif func==1:
#             print(username)
#             print(password)
#             SignIn()
#
#         else:
#             break
'''
登录练习结束
'''


# import  pickle  #序列化 dump() 和反序列 load() 化成二进制文件
# # var="I love You"
# # res=pickle.dumps(var)
# # res0=pickle.loads(res)
# # print(res,type(res))
# # print(res0,type(res0))
# vars = {'name':'张三','age':20,'sex':'m'}
# with open(r"2.txt","rb") as fp:
#     #pickle.dump(vars,fp)
#     res=pickle.load(fp)
#     print(res)


# import json
# var={'name': '张三', 'age': 20, 'sex': 'm'}
# var=(1,2,3)
# var="123"
# res=json.dumps(var)
# print(res,type(res))

# import math
# res=math.pow(2,3)
# print(res)


# import os
# os.system("dir")
# res=os.path.abspath("./2.txt")
# print(res)



'''
#高级文件操作模块
'''
# import  shutil
# # shutil.copy("1.txt",r"C:\Users\ruchan\Desktop\1.txt")  #复制文件
# shutil.move("1.txt",r"C:\Users\ruchan\Desktop\test\2.txt")


'''
压缩模块
'''
# import zipfile
# import os
# print(os.getcwd())
# # with zipfile.ZipFile("spam.zip","w") as myzip:
# #     myzip.write('2.txt')
# #     myzip.write("集合.png")
#
# with zipfile.ZipFile("spam.zip","r") as myzip:
#     myzip.extractall("./spam/")



# import time
# res=time.time()
# # print(time.ctime())
# print(time.ctime(res))
# print(time.localtime())
# res=time.strftime("%y-%m-%d %H:%M:%S")
# print(res)

import  calendar


import re
varstr="Iloveyou123 &loveu521ove2love234567"
# reg="love"
# res=re.findall(reg,varstr)
# res=re.match(reg,varstr)
# res=re.finditer(reg,varstr)
# res=re.sub(reg,"like",varstr)
# res=re.split(" ",varstr)

# print(res.group())
# res=re.search(reg,varstr)

# reg="\w" #一个字母，数字或者下划线
# reg="\w\d{2}"
#
# res=re.findall(reg,varstr)
# # res=re.search(reg,varstr)
# print(res)
#
# phone_num="15910573458"
# reg="^1\d{10}$"
# res=re.findall(reg,phone_num)
# print(res)
#
# var="iLoveYOu"
# reg="[a-z]{2,5}"
# res=re.findall(reg,var,re.I)
# print(res)

# 自定义异常日志处理类
# class Myexception():
#     def __init__(self):
#         import traceback
#         import logging
#
#         # logging的基本配置
#         logging.basicConfig(
#             filename='./error.log',# 日志存储的文件及目录
#             format='%(asctime)s  %(levelname)s \n %(message)s',# 格式化存储的日志格式
#             datefmt='%Y-%m-%d %H:%M:%S'
#         )
#         # 写入日志
#         logging.error(traceback.format_exc())
#
# # 使用自定义异常处理类
# try:
#     int('bb')
# except:
#     print('在此处进行异常的处理')
#     Myexception() # 在异常处理的代码块中去调用自定义异常类
#
# print('abcdef')

'''
为什么要用装饰器decorator https://www.bilibili.com/video/BV11s411V7Dt?from=search&seid=1928930556910434338 
'''
import time

def display_time(func):
    def wrapper(*args):
        t1=time.time()
        result=func(*args)
        t2=time.time()
        print(t2-t1)
        return result
    return  wrapper

def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return  True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False

        return True

@display_time
def prime_nums(maxnum):
    count=0
    for i in range(2,maxnum):
        if is_prime(i):
            print(i)
            count+=1
    return count

count=prime_nums(5000)
print(count)

