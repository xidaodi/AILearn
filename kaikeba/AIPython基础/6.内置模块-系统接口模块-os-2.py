# 系统接口模块 os

import os

# os.rmdir() 删除 空 文件夹
# os.rmdir('./a')  # a 是一个空文件夹
# os.rmdir('./b')  # b 是 含有一个文件夹的 目录 OSError: Directory not empty: './b'
# os.rmdir('./c')  # c 是 含有一个文件的  目录   OSError: [Errno 66] Directory not empty: './c'

# os.removedirs() 递归删除空文件夹
'''
连续创建几个空文件
abc/
    def/
        aaa/
./abc/def/aaa/

在mac系统中连续创建了abc目录后又在里面创建def，又在def里面创建aaa
此时。使用os.removedirs('./abc/def/aaa/') 删除时，只删除了aaa。
为什么？
因为mac系统中的文件夹只要被使用过，都会默认创建一个隐藏文件 .DS_Store，因此这个文件夹不在是空文件夹了

'''
# os.removedirs('./abc/def/aaa/')

# os.remove()  删除文件
# os.remove('./abc/.DS_Store')

# os.rename() 修改文件或文件夹的名字
# os.rename('./a','./AAA')


# os.system() 执行操作系统中的命令
os.system('python3 3.内置模块-数学模块-Math.py')
os.system('ls')



