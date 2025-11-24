# wap to accept an age from user if age<18 or age>60 raise custom exception with 
# message unusual age for job.

age=int(input("Enter the age: "))

try:
    if age<18 or age>60:
        raise ValueError
    else:
        print("Remaining years for job: ",60-age)
except ValueError:
    print("You are not valid for job")