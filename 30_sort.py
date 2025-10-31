#sorted(iterable, key=None, reverse=False)

lit=[10,3,56,34,9,0]
print(list(sorted(lit)))
#[0, 3, 9, 10, 34, 56]

print(list(sorted(lit,reverse=True)))
#[56, 34, 10, 9, 3, 0]

dict={
    'jan':2,
    'fab':67,
    'mar':34,
    'apr':7
}
print(list(sorted(dict,key=lambda x:dict[x])))
print(list(sorted(dict,key=lambda x:x[2])))

#without using key:['apr', 'fab', 'jan', 'mar']
#with key: ['jan', 'apr', 'mar', 'fab']
#['fab', 'jan', 'mar', 'apr']
