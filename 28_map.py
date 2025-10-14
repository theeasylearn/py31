#map(function, iterable, ...)

numbers=[1,2,3,4,5,6,7]
print(list(map(lambda n:n*n,numbers)))

#[1, 4, 9, 16, 25, 36, 49]

tup=(1,2,3,4,5)
print(list(map(lambda n:n+1,tup)))
#[2, 3, 4, 5, 6]

num1=[1,2,3]
num2=[10,20,30]
print(tuple(map(lambda x,y:x+y,num1,num2)))
#(11, 22, 33)