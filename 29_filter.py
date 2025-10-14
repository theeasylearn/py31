#filter(function, iterable)

lit=[1,2,3,4,5,6,7]
print(list(filter(lambda n:n%2==1,lit)))

#[1, 3, 5, 7]