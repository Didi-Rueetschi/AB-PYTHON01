# Date and Time 2. Teil

# Module time
import time

# Birthday
dztuple = 1979, 5, 7, 0, 0, 0, 0, 0, 0
print("Birth:", time.strftime("%d.%m.%Y", dztuple))
birth = time.mktime(dztuple)
ltbirth = time.localtime(birth)

# Current
lttoday = time.localtime()
print("Today:", time.strftime("%d.%m.%Y"))

# Calculate age
age = lttoday[0] - ltbirth[0]
if lttoday[1] < ltbirth[1] or \
         lttoday[1] == ltbirth[1] and \
         lttoday[2] < ltbirth[2]:
    age = age - 1
print("Age:", age)
