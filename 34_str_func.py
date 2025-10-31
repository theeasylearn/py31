name="The Easy Learn"

upperstr=name.upper()
print(upperstr)
#print(name.upper())
#THE EASY LEARN

lower=name.lower()
print(lower)
#the easy learn

print(name)
#The Easy Learn

print(name.isalnum())
#False

alnum='myPass1234'
print(alnum.isalnum())
#True

print(alnum.isalpha())
print(name.isalpha())

print(lower.islower())
#True

print(alnum.isnumeric())
#False

mystr='   '
print(name.isspace())
print(lower.isspace())
print(mystr.isspace())
#True

print(name.istitle())
#True

print(upperstr.isupper())
#True

password='my@password1234'
print(len(password))
#15
print(len(name))
#14

place=['bhavnagar','gujarat','india']

connector='-'
placestr=connector.join(place)
print(placestr)
#bhavnagar-gujarat-india