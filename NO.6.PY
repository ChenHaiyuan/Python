'''
题目：斐波那契数列。 
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
'''
#第一种方法
n = int(input('Please input a integer:'))
def fib(n):
    a = 1
    b = 1
    i = 0
    for i in range(n-2):
        c = a+b
        a = b
        b = c
        i += 1
    return a

print(fib(n))
'''
#使用递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)
print(fib(8))
