# While loop

i=12
while i*i <200:
    print("number:", i, ", Square:", i*i)
    i+=1
print("End")

i=12
while True:
    print("number:", i, ", Square:", i*i)
    i+=1
    if i*i>200:
        break
