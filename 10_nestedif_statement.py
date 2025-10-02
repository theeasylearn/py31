age=int(input("Enter your age: "))
nationality=input("Enter your nationality: ")
voter_id=input("Do you have voter id?: ")

if age>=18:
    print("You are eligible for votting at this age.")
    
    if nationality=="indian" or nationality=="Indian" or nationality=="INDIAN":
        print("Good ! you are indian. ")
        
        if voter_id=="yes" or voter_id=="Yes" or voter_id=="YES":
            print("ok! go for votting.")
            
        else:
            
            print("sorry you are not eligible because you don't have voter id.")
    else:
        print("sad! you are not indian.")
    
else:
    print("You are not eligible for votting at this age.")