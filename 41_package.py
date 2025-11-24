# import earth.asian
# import earth.european
# import earth.north_a

from earth import asian as ac
from earth import european as ec
from earth import north_a as na

# print(ac.asian_countries)
# print(ac.asc)
# print(ec.european_countries)
# print(na.north_american_countries)

print(ac.asian_countries[0:6])
print(ac.asc*2)
var=ac.asc.pop(1)
print(var)