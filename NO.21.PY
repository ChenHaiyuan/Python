'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个,第二天早上又将剩下的桃子吃掉一半，
又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
num = []
j = 1
for i in range(10):
    num.append(j)
    print('The %dth day remain have %d peaches!'%(10-i,j))
    j = (j+1)*2
print("This monkey has picked %d peach at the first day!"%(j/2-1))