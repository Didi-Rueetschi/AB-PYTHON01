# Date and Time

import time
print("Time in Seconds:", time.time())
lt = time.localtime()

year,month,day,hours,minutes,seconds,wkdaynr = lt[0:7]
wkday = ["Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday","Sunday"]
print("Date: {0:02d}.{1:02d}.{2:4d}".format(day,month, year))
print("Time 24h: {0:02d}:{1:02d}:{2:02d}".format(hours,minutes,seconds))
print(time.strftime("Time 12h:" "%I:%M:%S clock %p", lt))
print("weekday:", wkday[wkdaynr])
