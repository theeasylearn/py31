#Qs:1 print all elements

fruits = ["Mango", "Banana", "Guava", "Papaya", "Pomegranate"]

for fruit in fruits:
    print(fruit)

'''o/p:
Mango
Banana
Guava
Papaya
Pomegranate
'''

#Qs:2 count number of items

vegetables = ("Potato", "Tomato", "Onion", "Brinjal", "Okra")

count=0
for vege in vegetables:
    count+=1
print(count)

#o/p:5

#Qs:3 calculate total & Average

marks = {"Math": 88, "English": 75, "Science": 92, "History": 80, "Geography": 78, "Computer": 95}

total=0
count=0

for subject in marks:
    total=total+marks[subject]
    count+=1
print("Total: ",total)
print("Count: ",count)
average=total/count
print("Average: ",average)

#o/p:
# Total:  508
# Count:  6
# Average:  84.66666666666667