#with argument without return value

def pythagoras(a,b):
   res=(a**2+b**2)**0.5
   print(res)

a=int(input("Enter first value: "))
b=int(input("Enter first value: "))
pythagoras(a,b)

#with argument with return value

def pythagoras(a,b):
    res=(a**2+b**2)**0.5
    return res

a=int(input("Enter first value: "))
b=int(input("Enter first value: "))
result=pythagoras(a,b)
print(result)

#without argument without return value

def pythagoras():
    a=int(input("Enter first value: "))
    b=int(input("Enter first value: "))
    res=(a**2+b**2)**0.5
    print(res)

pythagoras()

#without argument with return value

def pythagoras():
    a=int(input("Enter first value: "))
    b=int(input("Enter first value: "))
    res=(a**2+b**2)**0.5
    return res

result=pythagoras()
print(result)