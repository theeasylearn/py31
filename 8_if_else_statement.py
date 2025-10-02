science=int(input("Enter your science mark: "))
maths=int(input("Enter your maths mark: "))
english=int(input("Enter your english mark: "))

total=science+maths+english

percentage=total/3
print("-------------------------Result-------------------------")
print("Math:",maths)
print("Science:",science)
print("English:",english)
print("Total: ",total)
print("Percentage: ",percentage,"%")
if percentage>=80:
    print("Very good!")
    
if percentage>=60 and percentage<80:
    print("Good")
else:
    print("Poor")
    
# Enter your science mark: 45
# Enter your maths mark: 67
# Enter your english mark: 23
# -------------------------Result-------------------------
# Math: 67
# Science: 45
# English: 23
# Total:  135
# Percentage:  45.0 %
# Poor
    