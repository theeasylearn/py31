import datetime

# def getDate():
#     date=int(input("Enter the date: "))
#     month=int(input("Enter the month: "))
#     year=int(input("Enter the year: "))
    
#     var=datetime.date(year,month,date)
#     print(var)

# getDate()

date1=input("Enter the date: ")
date2=input("Enter the date: ")

var=datetime.date.fromisoformat(date1)
var1=datetime.date.fromisoformat(date2)

if var>var1:
    print("person1 is younger")
elif var1>var:
    print("person2 is young")
else:
    print("Both have equal age")