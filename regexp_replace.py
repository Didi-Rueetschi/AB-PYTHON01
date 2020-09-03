# Regular Expressions

import re
tx = "house and mouse and louse"
print("0: Basistext", tx)
print("1: (re) ", re.sub("mouse","x",tx))
print("1: (replace)", tx.replace("mouse","x"))
print("2: (re) ", re.sub("[hm]ouse","x",tx))
print("2: (replace)", tx.replace("[hm]ouse","x"))
print("6: (re) ", re.sub("^.ouse","x",tx))
print("7: (re) ", re.sub(".ous$","x",tx))
