'''
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
'''
I = ['吴思琪','陈海源','basketball','football','lucky','money','healthy']
A = I[:]
A.append('我是新来的~请大家多多关照~')
print(I)
print(A)