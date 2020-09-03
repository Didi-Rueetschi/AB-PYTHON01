# CLI Parameters

import sys
l=len(sys.argv)
if l==1:
    print("no language selected")
else:
    for w in range(1, l):
        if "f" in sys.argv[w]:
            print("Bonjour")
        elif "e" in sys.argv[w]:
            print("G'day")
        else:
            print("Gute Tag")

#use the Terminal
#input: python CLI_parameter.py -e

