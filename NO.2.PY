i = int(input("Please input your profit in this month:"))
profit = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
pro = 0

for n in range(0,6):
    if i >= profit[n]:
        pro += (i - profit[n])*rate[n]  #每一次循环，累加相应阶段的利润
        print ((i - profit[n])*rate[n])   #打印每个阶段的利润
        i = profit[n]

print (pro) #Print the total profit