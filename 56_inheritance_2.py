#single level inheritance
class KB: #PARENT CLASS
    #define constructor
    def __init__(self,bytes):
        #create instance variable
        self.bytes = bytes
        print("KB class constructor called...")
    def getKB(self):
        #create local variable
        kilobytes = self.bytes / 1024
        return kilobytes 
class MB(KB): #CHILD CLASS
    def __init__(self,bytes):
        #calling parent class constructor
        super().__init__(bytes)
        print("MB class constructor called...")

    def getMB(self):
        megabytes = super().getKB() / 1024
        return megabytes
    
bytes = int(input("Enter bytes"))
k1 = KB(bytes) #call constructor
kilobytes = k1.getKB()

print("Kilo bytes = ",kilobytes)

m1 = MB(bytes) #call constructor
megabytes = m1.getMB()
print("mega bytes = ",megabytes)
