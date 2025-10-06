#Qs:1 write a program to count vowels in given string (a e i o u A E I O U) 

str=input("Enter the string: ")
count=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
         count+=1
print("Total number of vowels in a string: ",count)

'''o/p:
Enter the string: i am a student. i love coding.
Total number of vowels in a string:  10'''

#Qs:2 print 1 to 10 using for loop 
#range(initial,final+1,increment(default)/decrement)

for i in range(1,11):
    print(i)
    
'''
1
2
3
4
5
6
7
8
9
10
'''

#Qs:3 count even number between 1 t0 10

count=0
for i in range(1,11):
    if i%2==0:
        count+=1
        print(i)
print("Total even numbers: ",count)

'''
2
4
6
8
10
Total even numbers:  5
'''