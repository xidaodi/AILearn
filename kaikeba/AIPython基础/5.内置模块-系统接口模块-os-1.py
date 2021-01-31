# 系统接口模块 os

import os

# os.getcwd() 获取当前的工作目录,注意获取的不是当前脚本的目录，
res = os.getcwd()

# 如果在当前目录执行这个脚本文件，那么getcwd获取的就是当前的文件目录
# 如果把执行的目录切换到其它位置，在执行当前脚本，那么获取的就是你执行这个脚本时的目录

# os.chdir() # 修改当前的工作目录
# os.chdir('/Users/yc/')

# 修改工作目录后，再去获取工作目录
# res = os.getcwd()


# os.listdir() 获取当前或指定目录中的所有项（文件，文件夹，隐藏文件），组成的列表
# res = os.listdir() # 不指定目录时，默认为当前的工作目录  == linux 中的 ls -al   == windows dir
# res = os.listdir(path='/users/yc/Desktop/code') # == linux 中的 ls -al   == windows dir


# os.mkdir(文件夹路径，权限)  # 创建文件夹
# os.mkdir('aa',0o777)  # 默认在工作目录创建一个人文件夹

'''
    关于系统中的文件权限，仅限linux系统
    drwxr-xr-x   4 yc  staff   128 11 27 11:40 aa
    dr----x--x   2 yc  staff    64 11 27 11:42 abc
    第一位 d代表是一个目录，如果是-则表示为一个文件
    前三位的rwx 代表文件所有人( u )的权限
    中间三位的 r-x 代表文件所属组( g )的权限
    最后三位的 r-x 代表其他人( o )的权限
    
    其中 r w x 代表不同的操作权限  777 分别代表 所有人，所属组，和其它
    r 表示是否可读，   4
    w 表示是否可写     2
    x 表示是否可执行   1
'''
# os.mkdir('/users/yc/Desktop/code/abc/a/b/c') # 不能递归创建

# os.makedirs() 可以递归创建文件夹
# os.makedirs('/users/yc/Desktop/code/abc/a/b/c/')
# print(res)



