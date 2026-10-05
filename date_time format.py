#"Print today's,tomorrow,yesterday date in the format given below.

today = date.today()
 
print(today.strftime("Today it is %A %d %B %Y"))

yesterday = today - timedelta(days=1)
print(yesterday.strftime("Yesterday it was %A %d %B %Y"))

tomorrow = today + timedelta(days=1)
print(tomorrow.strftime("tomorrow is %A %d %B %Y"))
