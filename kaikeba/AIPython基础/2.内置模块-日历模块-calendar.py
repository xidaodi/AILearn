# 。calendar 日历模块

import  calendar

# 返回指定年份和月份的数据，月份的第一天是周几，和月份中的天数。
# calendar.monthrange（年，月）
def showdate(year,month):
    res = calendar.monthrange(year,month)
    days = res[1] # 当前月份的天数
    w = res[0]+1 # 当前月份第一天周几信息
    print(f'====={year}年{month}月的日历信息=====')
    print(' 一   二  三  四   五  六  日 ')
    print('*'*28)
    # 实现日历信息的输出
    d = 1
    while d <= days:
        # 循环周
        for i in range(1,8):
            # 判断是否输出
            if d > days or (i < w and d == 1):
                print(' '*4,end="")
            else:
                print(' {:0>2d} '.format(d),end="")
                d+=1
        print()
    print('*'*28)

showdate(2019,12)

# 作业练习：实现万年历  < 上一月  下一月 >
