#make sum and average of all numbers in list

numbers=['test',10,20,30,40,50,None]


sum=0
count=0

for i in numbers:
    try:
        sum=sum+i
        count=count+1
    except TypeError:
        print("Give only numbers")
print(sum)

ave=sum/count
print(ave)

#Give only numbers
# Give only numbers
# 150