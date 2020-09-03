# Error, except

# input
print ("Please enter number ")
z = input()

# Attempt to execute the function
try:
    number= int(z)
    print("correct input", number)
    print("that's the end of the try Block") #just executed if there is no Exception

# Error if function not executable
except:
    print("incorrect input", z)

print("after the try block")

