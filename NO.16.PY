'''
题目：输出指定格式的日期。
'''
import time
import datetime

#获取当前时间戳
ticks = time.time()
print(ticks)

if __name__ == '__main__':

#输出今日日期，格式为dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

#创建日期对象
    miyazakiBirthdate = datetime.date(1941,1,5)
    print(miyazakiBirthdate.strftime('%d/%m/%Y'))

#日期算术运算
    miyazakiBirthdate = miyazakiBirthdate + datetime.timedelta(days=100)
    print(miyazakiBirthdate.strftime('%d/%m/%Y'))

#日期替换
    miyazakiBirthdate = miyazakiBirthdate.replace(year=miyazakiBirthdate.year + 1)
    print(miyazakiBirthdate.strftime('%d/%m/%Y'))