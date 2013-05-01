from datetime import datetime

now = datetime.now()
print(now)
print(now.day)
print(now.month)
print str(now.month) + "/" + str(now.day) + "/" + str(now.year)
print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)