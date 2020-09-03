d= open("read.txt", "r+")
alllines = d.readlines()
print(d.tell()) # Indicate the position within the file
d.seek(0) # Jump to file begin

#Variant 1:
for lines in alllines:
    if "2.5" in lines:
        lines="8.5\n"
    d.write(lines)
d.close()


## Variant 2:
# d.seek(2)
# d.write('8')
# d.close()
