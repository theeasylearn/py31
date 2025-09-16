#working with string in python
#create string variable
name = "The Easylearn Academy"
address = """ 105,223, Eva surbhi, 
opp aksharwadi temple, 
Waghawadi road, 
Bhavnagar, Gujarat - 364001"""
print(name)
#print first letter in name variable T
print(name[0]) #T
print(name[1]) #h
print(name[4]) #e
print(name[0:5]) #The e
print(name[4:13]) #The easylearn
print(name[14:]) #The academy
print(name+address) 
print(name * 5) #print name variables 5 times
#we can replace string
name = 'T.E.L'
print(name)
# name[0] = 't' #error since string is immutable means we can not change part of the string
print("Good bye")