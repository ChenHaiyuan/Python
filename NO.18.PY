'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''
a = input('请输入一个数字：')
b = int(input('请输入几个数相加：'))
i = []
j = 0
sn = 0
while j < b:
    j += 1
    c = a*j
    i.append(c)
    print(c)
print(i)

for k in range(len(i)):
    d = int(i[k])
    sn += d

print(sn)