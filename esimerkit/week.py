import datetime

print("It'll be %s in a week." % (
	datetime.date.today() + 
	datetime.timedelta(days=7)
))