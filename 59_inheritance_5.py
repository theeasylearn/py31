#Hierarchical inheritance 
class Person: #parent
    def walk(self):
        print("I can walk...")
    def talk(self):
        print("I can talk...")
    def eat(self):
        print("I can eat...")

class Student(Person): #child
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #call parent class method
        super().walk()
        super().talk()
        super().eat()
        #calling same class method
        self.read()
        self.write()

class Artist(Person): 
    def act(self):
        print("I can do acting")
    def dance(self):
        print("I can dance")
        
#create person class object
p1 = Person()
p1.walk()
p1.talk()
p1.eat()

#create child class object
s1 = Student()
s1.whatICanDo()
s1.walk()
s1.talk()

#create artiest class object
a1 = Artist()
a1.act()
a1.dance()
a1.walk()
a1.talk()
a1.eat()
