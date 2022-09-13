from datetime import datetime, timedelta
time = datetime.today() + timedelta(hours=9)
print (time.strftime("%Y-%m-%d"))