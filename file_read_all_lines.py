# read complete file:
d = open("read.txt") #or.("read.txt","r")
alllines = d.readlines()
d.close()
for lines in alllines:
    print(lines[:-1]) #or.lines.replace("\n","")

# read sequential files:
d = open("read.txt")
lines = d.readline()
while lines:
    print(lines[:-1])
    lines = d.readline()
d.close()
