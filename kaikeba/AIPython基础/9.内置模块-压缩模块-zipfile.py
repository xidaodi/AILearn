#  压缩模块 zipfile

import zipfile,os

# 压缩文件 操作
# with zipfile.ZipFile('spam1.zip', 'w') as myzip:
#     myzip.write('data.json')
#     myzip.write('data.txt')
#     myzip.write('data2.txt')


# 解压缩文件
# with zipfile.ZipFile('spam.zip', 'r') as myzip:
#     myzip.extractall('./')


# 如果压缩当前文件夹中的所有文件？
# with zipfile.ZipFile('spam.zip', 'w',zipfile.ZIP_DEFLATED) as myzip:
#     # 获取当前目录中所有的项
#     arr = os.listdir('./')
#     for i in arr:
#         myzip.write(i)

# # 使用shutil模块进行归档压缩
# import shutil
# # 参数1 创建的压缩文件名称，参数2，指定的压缩格式，zip，tar 参数3 要压缩的文件或文件夹路径
# shutil.make_archive('a','zip','./')

