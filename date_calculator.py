from calendar import *
#这段代码定义的函数：day_in_a_week、distance_of_two_days、date_move、existed。
#在这段代码中，date2daycode和daycode2date是calendar内部的函数，Long_Gregorian_Calendar和Julian_Calendar是calendar内部的对象，由于第一行from calendar import *，“calendar.”已省略。
isgre=True
def day_in_a_week(date,isgre=True):
    curcal=Long_Gregorian_Calendar if isgre else Julian_Calendar
    #现行公历的1582年10月15日是星期五，在儒略历上是1582年10月5日
    if isgre:
        values=["星期五","星期六","星期天","星期一","星期二","星期三","星期四"]
    else:
        values=["星期三","星期四","星期五","星期六","星期天","星期一","星期二"]
    return values[date2daycode(date,curcal)%7]
def distance_of_two_days(date1,date2,isgre=True):
    curcal=Long_Gregorian_Calendar if isgre else Julian_Calendar
    return date2daycode(date2,curcal)-date2daycode(date1,curcal)
def date_move(date,delta,isgre=True):
    curcal=Long_Gregorian_Calendar if isgre else Julian_Calendar
    return daycode2date(date2daycode(date,curcal)+delta,curcal)
def existed(date, isgre=True):
    if isgre:
        leap=(date[0]%400==0) or (date[0]%100 and (date[0]%4==0))
    else:
        leap=(date[0]%4==0)
    days_in_months=(31,28+leap,31,30,31,30,31,31,30,31,30,31)
    if date[1]>12 or date[1]<1:
        return False
    elif date[2]>days_in_months[date[1]-1] or date[2]<1:
        return False
    else:
        return True
while 1:
    print()
    print("欢迎使用多功能日期计算器")
    print("1. 计算日期差")
    print("2. 日期推算")
    print("3. 星期查询")
    print("4. 特定日期（按照月、日、星期）搜索")
    if(isgre):
        print("5. 切换到儒略历（当前：现行公历）")
    else:
        print("5. 切换到现行公历（当前：儒略历）")
    print("6. 儒略历换算到现行公历")
    print("7. 现行公历换算到儒略历")
    print("0. 退出")
    op=input("请输入您的操作：")
    if op=="1":
        datetext1=input("请输入日期1（格式：年,月,日）：")
        datetext2=input("请输入日期2（格式：年,月,日）：")
        date1=[int(i) for i in datetext1.split(',')]
        date2=[int(i) for i in datetext2.split(',')]
        distance=distance_of_two_days(date1,date2,isgre)
        print(date1[0],"年",date1[1],"月",date1[2],"日",end=" 与 ")
        print(date2[0],"年",date2[1],"月",date2[2],"日",end=" 相差 ")
        print(distance,"天")
    elif op=="2":
        datetext1=input("请输入日期（格式：年,月,日）")
        delta=int(input("请输入加或减的天数（正数代表加，负数代表减，例如-1表示减1天，+3或3表示加3天）："))
        date1=[int(i) for i in datetext1.split(',')]
        date2=date_move(date1,delta,isgre)
        if delta>0:
            print(date1[0],"年",date1[1],"月",date1[2],"日",end=" + ")
            print(delta,"天",end=" = ")
        else:
            print(date1[0],"年",date1[1],"月",date1[2],"日",end=" - ")
            print(-delta,"天",end=" = ")
        print(date2[0],"年",date2[1],"月",date2[2],"日")
    elif op=="3":
        datetext1=input("请输入日期（格式：年,月,日）")
        date1=[int(i) for i in datetext1.split(',')]
        print(date1[0],"年",date1[1],"月",date1[2],"日",end=" 是 ")
        print(day_in_a_week(date1,isgre))
    elif op=="4":
        month=int(input("请输入月（0~12，其中0表示所有月份）："))
        day=int(input("请输入日（0~31，其中0表示这个月所有天；如果月和日都为0，表示本年所有天）："))
        dayweek=input("请输入星期（星期一/星期二/星期三/星期四/星期五/星期六/星期天）：")
        year1=int(input("请输入起始年份："))
        year2=int(input("请输入终止年份："))
        count=0
        if month:
            if day:
                print("以下是",month,"月",day,"日为",dayweek,"中自",year1,"年至",year2,"年的所有日期：")
                for i in range(year1,year2+1):
                    searchday=(i,month,day)
                    if existed(searchday,isgre):
                        if day_in_a_week(searchday,isgre)==dayweek:
                            print(searchday[0],"年",searchday[1],"月",searchday[2],"日")
                            count=count+1
            
            else:
                print("以下是",month,"月所有",dayweek,"中自",year1,"年至",year2,"年的所有日期：")
                for i in range(year1,year2+1):
                    if isgre:
                        leap=(i%400==0) or (i%100 and (i%4==0))
                    else:
                        leap=(i%4==0)
                    days_in_months=(31,28+leap,31,30,31,30,31,31,30,31,30,31)
                    for j in range(1,days_in_months[month-1]+1):
                        searchday=(i,month,j)
                        if day_in_a_week(searchday,isgre)==dayweek:
                            print(searchday[0],"年",searchday[1],"月",searchday[2],"日")
                            count=count+1
        else:
            if day:
                print("以下是",day,"日为",dayweek,"中自",year1,"年至",year2,"年的所有日期：")
                for i in range(year1,year2+1):
                    for j in range(1,13):
                        searchday=(i,j,day)
                        if existed(searchday,isgre):
                            if day_in_a_week(searchday,isgre)==dayweek:
                                print(searchday[0],"年",searchday[1],"月",searchday[2],"日")
                                count=count+1
            
            else:
                print("以下是所有",dayweek,"中自",year1,"年至",year2,"年的所有日期：")
                for i in range(year1,year2+1):
                    if isgre:
                        leap=(i%400==0) or (i%100 and (i%4==0))
                    else:
                        leap=(i%4==0)
                    days_in_months=(31,28+leap,31,30,31,30,31,31,30,31,30,31)
                    for j in range(1,13):
                        for k in range(1,days_in_months[j-1]+1):
                            searchday=(i,j,k)
                            if day_in_a_week(searchday,isgre)==dayweek:
                                print(searchday[0],"年",searchday[1],"月",searchday[2],"日")
                                count=count+1
        print("一共有",count,"个日期")
    elif op=="5":
        isgre=not isgre
    elif op=="6":
        datetext1=input("请输入儒略历日期（格式：年,月,日）")
        date1=[int(i) for i in datetext1.split(',')]
        print("儒略历",date1[0],"年",date1[1],"月",date1[2],"日",end=" 是现行公历 ")
        date2=relative_zeroth_day_convent(unconvented=date1,cal1=Julian_Calendar,cal2=Long_Gregorian_Calendar,zero1=(1582,10,5),zero2=(1582,10,15))
        print(date2[0],"年",date2[1],"月",date2[2],"日")
    elif op=="7":
        datetext1=input("请输入现行公历日期（格式：年,月,日）")
        date1=[int(i) for i in datetext1.split(',')]
        print("现行公历",date1[0],"年",date1[1],"月",date1[2],"日",end=" 是儒略历 ")
        date2=relative_zeroth_day_convent(unconvented=date1,cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5))
        print(date2[0],"年",date2[1],"月",date2[2],"日")
    elif op=="0":
        break
    else:
        print("没有这个操作！")