"""
Question:古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""
'''
递归解法
i = 1
j = 1
def fun(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fun(n-1) + fun(n-2)

print(fun(6))
'''
#循环解法
def Fibonacci_Loop_tool(n):
    a,b = 0,1
    while n > 0:
        a,b = b,a + b
        n -= 1
    return a
print(Fibonacci_Loop_tool(6))