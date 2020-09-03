# Return function
import math

def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

# Invoke function
f, u = circle(3)
print("area:", f)
print("circumference:", u)

# or
x = circle(3)
print("area:", x[0])
print("circumference:", x[1])
print(type(x))

