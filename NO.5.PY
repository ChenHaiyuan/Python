'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''



'''
#我的答案-------面向过程的编程
a = int(input('Please input the first integer:'))
b = int(input('Please input the second integer:'))
c = int(input("Please input the third integer:"))

if a > b:
    if a> c:
        if b > c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if a > c:
        print(b,a,c)
    else:
        if b > c:
            print(b,c,a)
        else:
            print(c,b,a)
'''

#面向对象编程
l = []
for i in range(1,4):
    a = int(input('请输入第%d个integer：'%i))
    l.append(a)
l.sort()
print(l)