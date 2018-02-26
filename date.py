import datetime

today = datetime.date.today()
if today.year > 2016:
    print("We're living in the now. It's", today.year)
else:
    print("We're living in the past")
