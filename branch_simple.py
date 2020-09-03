# Branching

# Set variables
c=50
print("Please enter a number ")
number= input("-> ")
number=int(number)

if number==c:
    print(number, "is correct")
elif number< 0 or number> 100:
    print(number, "is wrong, really wrong")
elif c-1 <= number and number<= c+1:
    print(number,"is pretty close")
else:
    print(number,"is wrong")
