dict={
    'property/key':'value',
    'name':'Drashti Mehta',
    'age':22,
    'institute':'the easy learn'
}

print(dict)
#o/p:{'property/key': 'value', 'name': 'Drashti Mehta', 'age': 22}

print(dict['name'])
#o/p:Drashti Mehta

dict['institute']='the easy learn acadamy'
print(dict)
#o/p:{'property/key': 'value', 'name': 'Drashti Mehta', 'age': 22, 'institute': 'the easy learn acadamy'}

del dict['institute']
print(dict)
#o/p:{'property/key': 'value', 'name': 'Drashti Mehta', 'age': 22}

#empty dictionary:
dict1={}
print(dict1)

dict1['school']='Gurukul'
dict1['Address']='Sardarnagar'
dict1['contact']=364789898578
print(dict1)
#o/p:{'school': 'Gurukul', 'Address': 'Sardarnagar', 'contact': 364789898578}

dict2={}
dict2['numbers']=(1,2,3,4)
dict2['characters']=['a','d','f','g']
print(dict2)
#o/p:{'numbers': (1, 2, 3, 4), 'characters': ['a', 'd', 'f', 'g']}
dict2['details']=dict1
print(dict2)
#o/p:{'numbers': (1, 2, 3, 4), 'characters': ['a', 'd', 'f', 'g'],
# 'details': {'school': 'Gurukul', 'Address': 'Sardarnagar', 'contact': 364789898578}}

dict2.clear()
print(dict2)
#o/p:{}

dict3=dict1.copy()
print(dict3)
#o/p:{'school': 'Gurukul', 'Address': 'Sardarnagar', 'contact': 364789898578}

print(dict1.get('Address',[404]))
#Sardarnagar
#o/p:[404]

print(dict1.items())
#o/p:dict_items([('school', 'Gurukul'),
# ('Address', 'Sardarnagar'), ('contact', 364789898578)])  

print(dict1.keys())     
#o/p:dict_keys(['school', 'Address', 'contact'])

seq={
    'num1':1,
    'num2':2,
    'num3':3
}
res=dict.fromkeys(seq,['number'])
print(res)
#o/p:{'num1': ['number'], 'num2': ['number'], 'num3': ['number']}

dict5={
    'name':'hello',
    'work':'xyz',
    'age':45
}
print(dict5.pop('age',['you']))
#o/p:45

print(dict5.popitem())
#o/p:('work', 'xyz')

#print(dict2.popitem())
#o/p:KeyError: 'popitem(): dictionary is empty.


dict6={
    'name':'hello',
    'work':'my work'
}
dict7={
    'name':'hello',
    'work':'xyz',
    'age':45
}
dict6.update(dict7)
print(dict6)
#o/p:{'name': 'hello', 'work': 'xyz', 'age': 45}


dict8={
    'contact':234545465,
    'address':'sjhfhgh'
}
print(dict8.values())
#o/p:dict_values([234545465, 'sjhfhgh'])
