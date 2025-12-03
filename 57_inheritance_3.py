#multilevel level inheritance
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

#inherit derived class (Developer)
class Developer(Student):
    def code(self):
        print("I can write code")
    def debug(self):
        print("I can debug code")
    def whatICanDo(self): #method Overidding
        super().whatICanDo() #calling parent class method
        self.code()
        self.debug()

#create object of Developer 
d1 = Developer()
d1.code()
d1.debug()
d1.whatICanDo() #calling child class method because object is child class
        