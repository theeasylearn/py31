#print hello message to many person using one function:

def sayhello(*names):
    
    for name in names:
        print("Hello to ",name)    
        
sayhello("Drashti","Vivek","Deep","Krisha","Salim")

#o/p:
# Hello to  Drashti
# Hello to  Vivek
# Hello to  Deep
# Hello to  Krisha
# Hello to  Salim    