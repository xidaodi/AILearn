# 。高级模块  shutil

import  shutil

# shutil == shell util

# copy 复制文件  把一个文件拷贝到指定的目录中
# shutil.copy('./data.json','./a/da.json')

# copy2 和copy方法一样，可以把拷贝文件到指定目录，保留了原文件的信息（操作时间和权限等）

# copyfile 拷贝文件的内容（打开文件，读取内容，写入到新的文件中）

# copytree 可以把整个目录结构和文件全部拷贝到指定目录中，但是要求指定的目标目录必须不存在
# shutil.copytree('./a','./b/')

# rmtree() 删除整个文件夹
# shutil.rmtree('./a')

# move 移动文件或文件夹到指定目录，也可以用于修改文件夹或文件的名称
shutil.move('./b','./abc')