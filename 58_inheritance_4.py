#multilevel inheritance
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
#inheriting derived class 
class GB(MB):
    def __init__(self, bytes):
        super().__init__(bytes) #calling parent class constructor
    def getGB(self):
        gigabytes = super().getMB() / 1024
        return gigabytes

bytes = int(input("Enter bytes"))
# create GB class object
g1 = GB(bytes)
gigabytes = g1.getGB()
megabytes = g1.getMB()
kilobytes = g1.getKB()
print(f"gigabytes = {gigabytes} megabytes = {megabytes} kilobytes = {kilobytes}")