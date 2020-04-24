'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

for n in range(2,1001):
    s = []
    j = 2
    for i in range(1,n):
        if n == sum(s):
            print(s)
            print(n)
            break 
        elif n % i == 0:
            s.append(i)
            i += 1
        else:
            continue