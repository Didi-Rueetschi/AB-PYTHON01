# Regular Expressions 2. Example

import re
y="In these 3 Streets there are 33 houses with 333 windows"
print("direct 33:", re.sub("33","65",y))
print("33+ :", re.sub('33+',"65",y))
print("33+? :", re.sub('33+?',"65",y))
print("3{2} :", re.sub('3{2}',"65",y))
print("33(?!3) :", re.sub('33(?!3)',"65",y))
print("\W33\W :", re.sub('\s33\s',"65",y))
print("Word limit:", re.sub('(?<=\s)33(?=\s)',"65",y))
