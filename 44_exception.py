#Write a program to findout and display cube of positive given number. 

#try:
    #statement
#except exception name:
    #exception handling code
#else:
    #statement
    
try:  
    n=int(input("Enter the number: "))
    cube=n*n*n
    print(cube)

except ValueError:
    print("Enter only integer numbers")
    
#print("bye")
else:    
    print("bye")