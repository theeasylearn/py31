#multiple inheritance 
class Email:
    def send(self):
        print("Email send")

class SMS:
    def send(self):
        print("SMS send")
    
#here class Communication has 2 parent Email & sms 
class Communication(Email,SMS):
    #Method Overidding
    def send(self):
        print("Sending message via email and sms .....")
        Email.send(self) #send method of Email will execute 
        SMS.send(self) #send method of SMS class will execute 
    
c1 = Communication()
c1.send() # will call send method of Communication class 
