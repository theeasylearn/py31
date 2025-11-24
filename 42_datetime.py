import datetime

date1=datetime.date(2012,12,4)
date2=datetime.date(2020,4,6)

print(date1>date2)
#False
print(date1<date2)
#True

dt1=datetime.datetime(2018,3,5,5,12,8)
dt2=datetime.datetime(2021,6,15,6,3,45)
gap=dt2-dt1
print(gap)
#1198 days, 0:51:37

td1=datetime.timedelta(days=13,hours=4,weeks=2)
td2=datetime.timedelta(days=25,hours=7,weeks=1)

diff=td2-td1
print(diff)
#5 days, 3:00:00

currenttime=datetime.datetime.now()
print(currenttime)
#2025-11-05 17:12:57.380517

today=datetime.date.today()
print(today)
#2025-11-05

dfd=datetime.date(2012,12,14)
format=dfd.strftime('%a-%m-%d-%Y')
print(format)
#Fri-12-14-2012