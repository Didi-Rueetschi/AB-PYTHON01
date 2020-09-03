# Lambda Function
import random

#Standard Lambda-Function
circlearea = lambda r : r*2*3.14
print (circlearea(3))

#Lambda with map-function
c=[72,97,108,108,111]
m = list(map(lambda x: (chr(x)), c))

print (m)

#Lambda with filter-function
ungrad = list(filter(lambda x: x % 2,
[random.randint(1,1000) for i in range(10)]))
print(ungrad)
