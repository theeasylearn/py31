lit=[3,'a',4.5,'hello',True]
lit1=[4,8.7,"f"]

print(lit)
#o/p: [3, 'a', 4.5, 'hello', True]

print(lit[3])
#o/p: hello

print(lit[1:3])
#o/p: ['a', 4.5]

print(lit[1:])
#o/p: ['a', 4.5, 'hello', True]

print(lit*2)
#o/p: [3, 'a', 4.5, 'hello', True, 3, 'a', 4.5, 'hello', True]

print(lit+lit)
print(lit+lit1)
#o/p: [3, 'a', 4.5, 'hello', True, 3, 'a', 4.5, 'hello', True]
#[3, 'a', 4.5, 'hello', True, 4, 8.7, 'f']

print(lit[:3])

lit.append(4)
print(lit)
#[3, 'a', 4.5, 'hello', True, 4]

lit1.extend([4,"r"])
print(lit1)
#[3, 'a', 4.5, 'hello', True, 4]

lit1.insert(2,'Drashti')
print(lit1)
#[4, 8.7, 'Drashti', 'f', 4, 'r']

lit.remove(3)
print(lit)
#['a', 4.5, 'hello', True, 4]

lit.remove(lit[3])
print(lit)
#['a', 4.5, 'hello', 4]

lit1.pop(2)
print(lit1)
#[4, 8.7, 'f', 4, 'r']

lit1.clear()
print(lit1)
#o/p:[]

lit2=['a',2,'abc',2,5.6,7]
print(lit2.index('a'))
#o/p:1

print(lit2.count(2))
#o/p:2

lit3=[3,5,10,34,1,2]
lit3.sort()
print(lit3)
#o/p:[1, 2, 3, 5, 10, 34]

lit3.reverse() 
print(lit3)
#o/p:[34, 10, 5, 3, 2, 1]

lit4=lit3.copy()
print(lit4)
#o/p:[34, 10, 5, 3, 2, 1]