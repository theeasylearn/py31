#Qs:1 fibbonacci:

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        result=fibo(n-1)+fibo(n-2)
        return result
n=4

for i in range(n):
     print(fibo(i))
     
#Qs:2 factorial:

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("Enter the value: "))
print(fact(n))