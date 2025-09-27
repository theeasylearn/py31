tup=(2,'w',3.4,False,'fdc')
tup1=('r','hello','r')

print(tup)
print(tup1)
#o/p:(2, 'w', 3.4, False, 'fdc')
#    ('r', 'hello')

print(tup[2])
#o/p:3.4

print(tup[1:4])
#o/p:('w', 3.4, False)

print(tup[1:])
#o/p:('w', 3.4, False, 'fdc')

print(tup1*2)
#o/p:('r', 'hello', 'r', 'hello')

print(tup+tup1)
#o/p:(2, 'w', 3.4, False, 'fdc', 'r', 'hello')

print(tup1.count('r'))
#o/p:2

print(tup.index(False))
#o/p:3  