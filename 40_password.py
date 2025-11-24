import random
import string

def randomPass(passlen=8):
    
    chars=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    password=[]
    
    for i in range(passlen):
        str=chars[random.randint(0,passlen)]
        password.append(str)
    str=''
    print(str.join(password))
    
passlen=int(input("Enter the length of password: "))
randomPass(passlen)