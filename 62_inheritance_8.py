#hybrid inheritance 
class MyMath:
    def __init__(self,number):
        self.number = number
        print("MyMath class constructor called...")
    def getSquare(self):
        square = self.number * self.number
        return square
class Trigonomatry:
    def getPi(self):
        temp = 22/7.0
        return temp 
class Cyliender(MyMath,Trigonomatry):
    def __init__(self,radius,height):
        #calling parent constructor 
        MyMath.__init__(self,radius)
        self.radius = radius 
        self.height = height 
        print("Cyliender class constructor called...")
    def getVolume(self):
        volume = super().getPi() * super().getSquare() * self.height
        return volume

class Cone(Cyliender):
    def __init__(self, radius, height):
        super().__init__(radius, height)
    def getVolume(self):
        volume = (1/3) * super().getVolume()
        return volume

radius = int(input("Enter radius"))
height = int(input("Enter height"))
c2 = Cone(radius,height)
print(c2.getVolume())

