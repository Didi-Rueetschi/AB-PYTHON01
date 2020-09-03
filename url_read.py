import urllib.request
# Connection to URL
u = urllib.request.urlopen("http://www.cssgmbh.ch/cssgmbh/Beispiele/url_lesen.htm")
# Read all lines in a list
li = u.readlines()
# Close connection
u.close()
# Output list
for element in li:
    print(element)
