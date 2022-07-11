import random
import string

#Password lenght
x = int(input("How many characters do you want to create a password?:\n "))

#Definition of the function that generates 
#random string of the specified number of lengths
def generatePass(x):
    
    randlist = ""
    
    for i in range(x):    
        randlist += random.choice(string.printable[0:string.printable.index("~")+1])

    print(randlist)
        

generatePass(x)
