'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

string = input('Please input a str:')
letters = []
space = []
digit = []
others = []
i = 0
while i < len(string):
    c = string[i]
    i += 1
    if c.isalpha():
        letters.append(c)
    elif c.isspace():
        space.append(c)
    elif c.isdigit():
        digit.append(c)
    else:
        others.append(c)

print("letters = ",letters)
print("space = ",space)
print("digit = ",digit)
print("others = ",others)
#Python3 格式化输出时，双引号""和后面的%号之间是没有逗号，的。
print("letters = %d, space = %d, digit = %d, others = %d"%(len(letters),len(space),len(digit),len(others)))

