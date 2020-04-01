'''
Question:题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
'''
i=0
nb=[]
for sqrt in range(101,201):
    y = 1
    for n in range(2,sqrt):
        if sqrt % n == 0:
            y = 0
            i += 1
            break
    if y == 1:
        nb.append(sqrt)
print(nb)
print(100-i)