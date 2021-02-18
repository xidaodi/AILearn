# 自定义异常处理类

'''
在出现异常后，对异常进行处理。并且把异常信息写入日志
日志的基本格式：
    日期时间 异常的级别
    异常信息：引发的异常类，异常的信息，文件及行号。。
'''
import traceback
import logging


# int('aa')

# try:
#     int('aa')
# except:
#     # 通过 traceback 模块获取异常信息
#     errormsg = traceback.format_exc()
#     print(errormsg)


# 自定义异常日志处理类
class Myexception():
    def __init__(self):
        import traceback
        import logging

        # logging的基本配置
        logging.basicConfig(
            filename='./error.log',# 日志存储的文件及目录
            format='%(asctime)s  %(levelname)s \n %(message)s',# 格式化存储的日志格式
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        # 写入日志
        logging.error(traceback.format_exc())

# 使用自定义异常处理类
try:
    int('bb')
except:
    print('在此处进行异常的处理')
    Myexception() # 在异常处理的代码块中去调用自定义异常类

print('abcdef')



