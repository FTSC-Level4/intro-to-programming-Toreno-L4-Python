from datetime import datetime

now = datetime.now()
timedate = now.strftime("%d/%m/%Y and %H:%M:%S")

print("The date and time for today is", timedate)