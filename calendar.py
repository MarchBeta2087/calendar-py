class Calendar:
    def __init__(self,layers,period,mid_periods,year_months):
        self.layers=layers #多层周期的层数，类型一般为整数
        self.period=period #大周期，类型一般为2重嵌套元组
        self.mid_periods=mid_periods #多层周期，类型一般为4重嵌套元组（layers为0时，mid_period为单重空白元组“()”）
        self.year_months=year_months #年，类型一般为2重嵌套元组
    def __hash__(self):
        return hash((self.layers,self.period,self.mid_periods,self.year_months))&2147483647
    def __eq__(self,other):
        return ((self.layers==other.layers) and (self.period==other.period) and (self.mid_periods==other.mid_periods) and (self.year_months==other.year_months))
    def __ne__(self,other):
        return (not (self==other))
nonleap_year_months=(0,31,59,90,120,151,181,212,243,273,304,334,365) #非闰年
leap_year_months=(0,31,60,91,121,152,182,213,244,274,305,335,366) #闰年
Gregorian_year_months=(nonleap_year_months,leap_year_months)
leap4=((1,0,0),(0,1,366),(0,2,731),(0,3,1096),(0,4,1461)) #有闰年的4年
nonleap4=((0,0,0),(0,1,365),(0,2,730),(0,3,1095),(0,4,1460)) #没有闰年的4年
year4=(leap4,nonleap4)
centurynon400=((1,0,0),(0,4,1460),(0,8,2921),(0,12,4382),(0,16,5843),(0,20,7304),(0,24,8765),(0,28,10226),(0,32,11687),(0,36,13148),(0,40,14609),(0,44,16070),(0,48,17531),(0,52,18992),(0,56,20453),(0,60,21914),(0,64,23375),(0,68,24836),(0,72,26297),(0,76,27758),(0,80,29219),(0,84,30680),(0,88,32141),(0,92,33602),(0,96,35063),(0,100,36524))
#有24个闰年的100年
century400=((0,0,0),(0,4,1461),(0,8,2922),(0,12,4383),(0,16,5844),(0,20,7305),(0,24,8766),(0,28,10227),(0,32,11688),(0,36,13149),(0,40,14610),(0,44,16071),(0,48,17532),(0,52,18993),(0,56,20454),(0,60,21915),(0,64,23376),(0,68,24837),(0,72,26298),(0,76,27759),(0,80,29220),(0,84,30681),(0,88,32142),(0,92,33603),(0,96,35064),(0,100,36525))
#有25个闰年的100年
year100=(centurynon400,century400)
year400=((1,0,0),(0,100,36525),(0,200,73049),(0,300,109573),(0,400,146097))

#Gregorian Calendar（格里高历），即现行公历，能被4整除但不能被100整除的年份是闰年，不能被4整除的年份是平年，能被100整除但不能被400整除的是平年，能被400整除的年份是闰年
Long_Gregorian_Calendar=Calendar(2,year400,(year100,year4),Gregorian_year_months)

#Julian Calendar（儒略历），与现行公历相比有着更简单的规则，能被4整除的年份是闰年
Julian_Calendar=Calendar(0,leap4,tuple(),Gregorian_year_months)
def showparts(layernum, index, cal=Long_Gregorian_Calendar, firsts=0, lasts=0):
    p=cal.period
    mp=cal.mid_periods
    la=cal.layers
    ym=cal.year_months
    if layernum<la:
        layerlen=len(mp[layernum][index])
        if firsts==0 and lasts==0:
            for k in range(layerlen):
                nextindex = mp[layernum][index][k][0]
                print("\t"*(layernum+1),"L",mp[layernum][index][k][1],"/",mp[layernum][index][-1][1],"年",mp[layernum][index][k][2],"/",mp[layernum][index][-1][2],"天")
                if k<layerlen-1:
                    showparts(layernum+1, nextindex, cal, firsts, lasts)
        else:
            for k in range(min(firsts,layerlen)):
                nextindex = mp[layernum][index][k][0]
                print("\t"*(layernum+1),"L",mp[layernum][index][k][1],"/",mp[layernum][index][-1][1],"年",mp[layernum][index][k][2],"/",mp[layernum][index][-1][2],"天")
                showparts(layernum+1, nextindex, cal, firsts, lasts)
            if len(mp[layernum][index])>firsts+lasts:
                print("\t"*(layernum+1),"…")
            for k in range(max(firsts,layerlen-lasts),layerlen):
                nextindex = mp[layernum][index][k][0]
                print("\t"*(layernum+1),"L",mp[layernum][index][k][1],"/",mp[layernum][index][-1][1],"年",mp[layernum][index][k][2],"/",mp[layernum][index][-1][2],"天")
                if k<layerlen-1:
                    showparts(layernum+1, nextindex, cal, firsts, lasts)
    else:
        for k in range(1,len(ym[index])):
            print("\t"*(la+1),"L",k,"月",ym[index][k]-ym[index][k-1],"天")
def showstruct(cal=Long_Gregorian_Calendar, firsts=0, lasts=0):
    p=cal.period
    for i in range(len(p)):
        print("L",p[i][1],"/",p[-1][1],"年",p[i][2],"/",p[-1][2],"天")
        if i<len(p)-1:
            showparts(0,p[i][0],cal,firsts,lasts)
    print()
#短日期：年,月,日（Gregorian Calendar，即现行公历）
#长日期：400年周期(0,1,2,3,4,5,6,7,...),100年周期(0,100,200,300),4年周期(0,4,8,12,...,92,96),年(0,1,2,3),月,日（现行公历）
#需要注意的是，现行公历以短日期表示，长日期只是一种“中间产物”
#短日期->长日期示例：2027,1,22->5,0,24,3,1,22（现行公历）
#长日期->短日期示例：4,300,92,2,11,26->1994,11,26（现行公历）
#下列函数可以将长日期和短日期相互转换
def long2short(longdate,cal=Long_Gregorian_Calendar):
    return (longdate[0]*cal.period[-1][1]+sum(longdate[1:-2]),longdate[-2],longdate[-1])
def short2long(shortdate,cal=Long_Gregorian_Calendar):
    yearcode=shortdate[0]
    periodcode=yearcode//cal.period[-1][1]
    remainyear=yearcode%cal.period[-1][1]
    cutyears=0
    sign=0
    for i in cal.period:
        if i[1]<=remainyear:
            cutyears=i[1]
            sign=i[0]
        else:
            break
    p2=[periodcode,cutyears]
    remainyear2=remainyear-cutyears
    pmid=[0 for _ in range(cal.layers)]
    for i in range(cal.layers):
        cut2=0
        place=0
        signtemp=0
        for j in cal.mid_periods[i][sign]:
            if j[1]<=remainyear2:
                signtemp=j[0]
                cut2=j[1]
                place=place+1
            else:
                sign=signtemp
                pmid[i]=cut2
                remainyear2=remainyear2-cut2
                break
    last2=[shortdate[-2],shortdate[-1]]
    return tuple(p2+pmid+last2)
#在现行公历中，以0年1月1日为第1天，我们可以算出1年1月1日为第367天，1900年1月1日为第693962天，2000年1月1日为第730486天，等等
#下列函数可以将长日期和编码相互转换
def longdate2daycode(longdate,cal=Long_Gregorian_Calendar):
    daycode=cal.period[-1][2]*longdate[0]
    sign=0
    for i in cal.period:
        if i[1]==longdate[1]:
            daycode=daycode+i[2]
            sign=i[0]
            break
    for i in range(cal.layers):
        for j in cal.mid_periods[i][sign]:
            if longdate[i+2]==j[1]: #根据长日期上的数字累加天数
                daycode=daycode+j[2]
                sign=j[0]
                break
    daycode=daycode+cal.year_months[sign][longdate[-2]-1]
    daycode=daycode+longdate[-1]
    return daycode
def daycode2longdate(daycode,cal=Long_Gregorian_Calendar):
    longdate=[0 for i in range(cal.layers+4)]
    dayfromfirst=daycode-1
    periodcode=dayfromfirst//cal.period[-1][2] #确定长日期第一个数字
    longdate[0]=periodcode
    remain=dayfromfirst%cal.period[-1][2]
    cutdays=0
    cutyears=0
    sign=0
    for i in cal.period:
        if i[2]<=remain:
            cutdays=i[2]
            cutyears=i[1] #确定长日期第二个数字
            sign=i[0]
        else:
            break
    longdate[1]=cutyears
    remain2=remain-cutdays
    for i in range(cal.layers):
        cuttemp=0
        temp=0
        signtemp=0
        for j in cal.mid_periods[i][sign]:
            if j[2]<=remain2:
                cuttemp=j[2]
                temp=j[1]
                signtemp=j[0]
            else:
                longdate[i+2]=temp
                sign=signtemp
                remain2=remain2-cuttemp
                break
    monthtemp=0
    months_in_the_year=cal.year_months[sign]
    for i in range(len(months_in_the_year)):
        if months_in_the_year[i]<=remain2:
            monthtemp=i+1
        else:
            longdate[-2]=monthtemp
            longdate[-1]=remain2-months_in_the_year[monthtemp-1]+1
            break
    return tuple(longdate)
#长日期只是一种“中间产物”，而我们通常使用短日期。下列函数可以将短日期和编码相互转换
def date2daycode(date,cal=Long_Gregorian_Calendar):
    return longdate2daycode(short2long(date,cal),cal)
def daycode2date(daycode,cal=Long_Gregorian_Calendar):
    return long2short(daycode2longdate(daycode,cal),cal)
#将一个日期从一套历法转换为另一套历法
def relative_zeroth_day_convent(unconvented=(1732,2,22),cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5)):
    code1=date2daycode(zero1,cal1)
    code2=date2daycode(zero2,cal2)
    return daycode2date(date2daycode(unconvented,cal1)+(code2-code1),cal2)
#使用下面这个函数可组装成year_months，days_of_months需填入一个2重元组，例如days_of_months为((3,4,4),(3,2,2))时，返回((0,3,7,11),(0,3,5,7))
def year_month_sum(days_of_months):
    year_months=[]
    for i in days_of_months:
        months=len(i)
        months_in_one_year=[0 for _ in range(months+1)]
        su=0
        for j in range(months):
            su=su+i[j]
            months_in_one_year[j+1]=su
        year_months.append(tuple(months_in_one_year))
    return tuple(year_months)
#使用这个函数可组装成year_months的最低层（3重元组），sumtables为2重元组，signtables为2重元组，例如sumtables为((0,3,7,11),(0,3,5,7))，signtables为((0,1,1),(1,0,0))时，返回(((0,0,0),(1,1,11),(1,2,18),(0,3,25)),((1,0,0),(0,1,7),(0,2,18),(0,3,29)))
def mid_periods_first_layer_assemblation(sumtables,signtables):
    yearlists=tuple([i[-1] for i in sumtables])
    mid_periods_first=[]
    for i in signtables:
        part=[]
        day=0
        year=0
        for j in i:
            part.append((j,year,day))
            day=day+yearlists[j]
            year=year+1
        part.append((0,year,day))
        mid_periods_first.append(tuple(part))
    return tuple(mid_periods_first)
#使用这个函数可组装成year_months的第二层、第三层、...（3重元组），low_layer为3重元组，signtables为2重元组，例如sumtables为(((0, 0, 0), (1, 1, 11), (1, 2, 18), (0, 3, 25)), ((1, 0, 0), (0, 1, 7), (0, 2, 18), (0, 3, 29)))，signtables为((0,1,1),(1,0,0))时，返回(((0,0,0),(1,3,25),(1,6,54),(0,9,83)),((1,0,0),(0,3,29),(0,6,54),(0,9,79)))
def mid_periods_high_layer_assemblation(low_layer,signtables):
    yearlists=tuple([i[-1][1] for i in low_layer])
    daylists=tuple([i[-1][2] for i in low_layer])
    mid_periods_first=[]
    for i in signtables:
        part=[]
        day=0
        year=0
        for j in i:
            part.append((j,year,day))
            day=day+daylists[j]
            year=year+yearlists[j]
        part.append((0,year,day))
        mid_periods_first.append(tuple(part))
    return tuple(mid_periods_first)
#使用这个函数可组装成period（2重元组），top_mid_periods为3重元组，signtable为单重元组
def period_assemblation(top_mid_periods,signtable):
    yearlists=tuple([i[-1][1] for i in top_mid_periods])
    daylists=tuple([i[-1][2] for i in top_mid_periods])
    mid_periods_first=[]
    day=0
    year=0
    for j in signtable:
        mid_periods_first.append((j,year,day))
        day=day+daylists[j]
        year=year+yearlists[j]
    mid_periods_first.append((0,year,day))
    return tuple(mid_periods_first)
#使用这个函数可组装一个Calendar类型对象，days_of_months为2重元组，mid_periods_signtables为3重元组（从低层到高层），period_signtable为单重元组
def assemblation(days_of_months,mid_periods_signtables,period_signtable):
    year_months=year_month_sum(days_of_months)
    layers=len(mid_periods_signtables)
    mid_periods=[]
    mid_periods_LE=[]
    if layers == 0:
        period=mid_periods_first_layer_assemblation(year_months,(period_signtable,))[0]
        assembled=Calendar(0,period,tuple(),year_months)
        return assembled
    elif layers == 1:
        firstlayer=mid_periods_first_layer_assemblation(year_months,mid_periods_signtables[0])
        period=period_assemblation(firstlayer,period_signtable)
        assembled=Calendar(1,period,(firstlayer,),year_months)
        return assembled
    else:
        firstlayer=mid_periods_first_layer_assemblation(year_months,mid_periods_signtables[0])
        low_layer=firstlayer
        high_layer=()
        for i in mid_periods_signtables[1::]:
            high_layer=mid_periods_high_layer_assemblation(low_layer,i)
            low_layer=high_layer
            mid_periods_LE.append(high_layer)
        mid_periods=tuple(reversed(mid_periods_LE))+(firstlayer,)
        period=period_assemblation(mid_periods[0],period_signtable)
        assembled=Calendar(layers,period,mid_periods,year_months)
        return assembled
