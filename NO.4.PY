'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
'''
#原答案......
year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))

#每个月的累加天数
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    n = months[month - 1]
else:
    print("data error")
n += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):    #判断是否为闰年
    leap = 1
if (leap == 1) and (month > 2):
    n += 1
print ("It is the %dth day." %n)
'''
#自己的代码
#每个月的累加天数
months = (0,31,59,90,120,151,181,212,243,273,304,334)
month_30 = [4,6,9,11]
month_31 = [1,3,5,7,8,10,12]
leap = 0
n = 0

year = int(input('Please input the year:'))
month = int(input('Please input the month:'))
if 0<month<13:
    day = int(input('Please input the day:'))
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):    #闰年
        leap = 1
        if month in month_30:
            if 1 <= day <= 30:
                n = months[month - 1] + day + leap
            else:
                print('The day you input is error!')
        elif month in month_31:
            if 1 <= day <= 31:
                if month <= 2:
                    n = months[month - 1] + day 
                else :
                    n = months[month - 1] + day + leap
            else:
                print('The day you input is error!')
        else:
            if 1 <= day <= 29:
                 n = months[month - 1] + day 
            else:
                print('The day you input is error!')

    else:                                                       #平年
        if month in month_30:
            if 1 <= day <= 30:
                n = months[month - 1] + day 
            else:
                print('The day you input is error!')
        elif month in month_31:
            if (1 <= day <= 31):
                if month <= 2:
                    n = months[month - 1] + day 
                else :
                    n = months[month - 1] + day 
            else:
                print('The day you input is error!')
        else:
            if 1 <= day <= 28:
                 n = months[month - 1] + day 
            else:
                print('The day you input is error!')
                
    print ("It is the %dth day." %n)
else:
    print("Sorry~The month you intput is wrong！")

        
        
    
    
