'''
题目：暂停一秒输出，并格式化当前时间。
'''
'''
#My answer~
import time

I = ['NI','HAO','MA',1,3,4,5,6,78,23,96,4,3]

for i in I:
    print(i)
    time.sleep(1)
'''
import time
#获取本地时间并整理成相应格式打印出来
#根据格式规范将时间元组转换为字符串。当时间元组不存在时，将使用localtime()返回的当前时间。
T = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(T)

#暂停5秒
time.sleep(5)
T = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(T)