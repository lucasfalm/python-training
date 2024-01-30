import datetime

today = datetime.date.today()
today.year
today.month
today.day

tomorrow = today + datetime.timedelta(days = 1)
tomorrow.year
tomorrow.month
tomorrow.day

yesterday = today + datetime.timedelta(days = -1)
yesterday.year
yesterday.month
yesterday.day
