from calendar import *
custom_example_months1=(0,4,9,12)
custom_example_months2=(0,4,9,14)
custom_example_year_months=(custom_example_months1,custom_example_months2)
custom_example_year2_1=((0,0,0),(1,1,12),(0,2,26))
custom_example_year2_2=((0,0,0),(0,1,12),(0,2,24))
custom_example_year2=(custom_example_year2_1,custom_example_year2_2)
custom_example_year12=((0,0,0),(0,2,26),(1,4,52),(0,6,76),(0,8,102),(0,10,128),(0,12,154))
# Lumeris
custom_example=Calendar(1,custom_example_year12,(custom_example_year2,),custom_example_year_months) #自定义1
# Caldaris
custom_example2_months1=(0,2,4,7)
custom_example2_months2=(0,2,5,7)
custom_example2_year_months=(custom_example2_months1,custom_example2_months2)
custom_example2_year2=((0,0,0),(1,1,7),(0,2,14))
custom_example2=Calendar(0,custom_example2_year2,tuple(),custom_example2_year_months) #自定义2
# Xalbrund
custom_example3_months1=(0,1,3)
custom_example3_year_months=(custom_example3_months1,)
custom_example3_year2=((0,0,0),(0,1,3),(0,2,6))
custom_example3=Calendar(0,custom_example3_year2,tuple(),custom_example3_year_months) #自定义3
# Mysira
custom_example4=assemblation(((3,4,4),(4,3,2)),(((0,1,1,0),(1,0,0)),((0,1,1),(1,0,0)),((0,1,1),(1,0,0))),(0,1,1,0,1))#自定义4
# Iskora
custom_example5=assemblation(((39,42,30,38,21,20),(200,260,230)),(((0,1,1,0),(1,0,0)),((0,1,1),(1,0,0)),((0,1,1),(1,0,0))),(0,1,1,0,1))#自定义5
showstruct(custom_example)
showstruct(custom_example2)
showstruct(custom_example3)
showstruct(custom_example4)
showstruct(custom_example5)
showstruct(Julian_Calendar)
showstruct(Long_Gregorian_Calendar,3,2)

#1582年10月15日在儒略历中是1582年10月5日，在现行公历的编码是578102，在儒略历的编码是578104
print(date2daycode((1582,10,15))) #578102
print(date2daycode((1582,10,5), Julian_Calendar)) #578104

#现行公历->儒略历
gre1=(1582,10,15)
gre2=(1732,2,22)
gre3=(2009,5,10)
print(gre1, "现行公历->儒略历", relative_zeroth_day_convent(unconvented=gre1,cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5)))
print(gre2, "现行公历->儒略历", relative_zeroth_day_convent(unconvented=gre2,cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5)))
print(gre3, "现行公历->儒略历", relative_zeroth_day_convent(unconvented=gre3,cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5)))

#儒略历->现行公历
ju1=(2008,7,23)
ju2=(2010,3,20)
print(ju1, "儒略历->现行公历", relative_zeroth_day_convent(unconvented=ju1,cal1=Julian_Calendar,cal2=Long_Gregorian_Calendar,zero1=(1582,10,5),zero2=(1582,10,15)))
print(ju2, "儒略历->现行公历", relative_zeroth_day_convent(unconvented=ju2,cal1=Julian_Calendar,cal2=Long_Gregorian_Calendar,zero1=(1582,10,5),zero2=(1582,10,15)))

#现行公历->各种历法（下述历法中，除儒略历和现行公历（格里高历）外，其他历法是虚构的，仅仅是为了测试）
gre4=(2027,1,22)
print(gre4, "现行公历->儒略历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=Julian_Calendar,zero1=(1582,10,15),zero2=(1582,10,5)))
print(gre4, "现行公历->Lumeris历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=custom_example,zero1=(2023,4,15),zero2=(2000,1,1)))
print(gre4, "现行公历->Caldaris历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=custom_example2,zero1=(2015,1,1),zero2=(1,1,1)))
print(gre4, "现行公历->Xalbrund历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=custom_example3,zero1=(1996,1,1),zero2=(1,1,1)))
print(gre4, "现行公历->Mysira历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=custom_example4,zero1=(2008,1,1),zero2=(2600,1,1)))
print(gre4, "现行公历->Iskora历", relative_zeroth_day_convent(unconvented=gre4,cal1=Long_Gregorian_Calendar,cal2=custom_example5,zero1=(2023,1,1),zero2=(2018,1,1)))

print("现行公历的hash",hex(hash(Long_Gregorian_Calendar)))
print("儒略历的hash",hex(hash(Julian_Calendar)))
print("儒略历==儒略历","->",Julian_Calendar==Julian_Calendar)
print("儒略历!=儒略历","->",Julian_Calendar!=Julian_Calendar)
print("儒略历==现行公历","->",Julian_Calendar==Long_Gregorian_Calendar)
print("儒略历!=现行公历","->",Julian_Calendar!=Long_Gregorian_Calendar)
print("儒略历hash==儒略历hash","->",hash(Julian_Calendar)==hash(Julian_Calendar))
print("儒略历hash!=儒略历hash","->",hash(Julian_Calendar)!=hash(Julian_Calendar))
print("儒略历hash==现行公历hash","->",hash(Julian_Calendar)==hash(Long_Gregorian_Calendar))
print("儒略历hash!=现行公历hash","->",hash(Julian_Calendar)!=hash(Long_Gregorian_Calendar))