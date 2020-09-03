# Output and formatting

print ("{0:<4}{1:>9}{2:>4}{3:>4}{4:>8}".format
("dec", "dual", "oct", "hex", "Float"))
fm="{0:<4d}{1:>9b}{2:>4o}{3:>4x}{4:>8.2f}"
for z in range(62,66):
    print(fm.format(z,z,z,z,z))
