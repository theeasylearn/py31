details={1,'girl',('shivani','sneha')}
print(details)
#o/p:{1, ('shivani', 'sneha'), 'girl'}

details.add('employee')
print(details)
#o/p:{1, 'employee', ('shivani', 'sneha'), 'girl'}

details.remove('employee')
print(details)
#o/p:{('shivani', 'sneha'), 1, 'girl'}

set1={1,2,3,4,5}
set2={1,2,3,6,9}

result=set2.union(set1)
print(result)
#o/p:{1, 2, 3, 4, 5, 6, 9}

result1=set2.intersection(set1)
print(result1)
#o/p:{1, 2, 3}

result2=set1.difference(set2)
print(result2)
#o/p:{4, 5}/result2=set2.difference(set1):=>{9, 6}