# For loop

for i in range(12,20):
    if i*i > 200:
        print("number", i, "is too big")
        break
    print("number:", i, ", Square:", i*i)
print("this statement is out of the loop block")
