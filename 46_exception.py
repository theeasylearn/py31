try:
    num1=int(input("Enter first numbe:"))
    num2=int(input("Enter second numbe:"))

    div=num1/num2
    print(div)
    
#except (ZeroDivisionError,ValueError):   
except ZeroDivisionError:
    print("number can not divide by zero")
except ValueError:
    print("Input only integer value")

except Exception as e:
    print("something went wrong",e)