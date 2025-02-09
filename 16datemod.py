import datetime

d = datetime.date (2016,7,24)
print(d)

tday = datetime.date.today()
print(tday.weekday()) # Monday = 0, Sunday = 6
print(tday.isoweekday()) # Monday = 1, Sunday = 7

tdelta = datetime.timedelta(days=7) # adding 7 days
print(tday + tdelta) # adding 7 days to current date
print(tday - tdelta) # subtracting 7 days from current date\\
    
bday = datetime.date(2004, 6, 18)
till_bdy = bday - tday
print(till_bdy.total_seconds())
print(till_bdy.days)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.time())
print(dt.date())
tdel = datetime.timedelta(hours=12)
print(dt + tdel)


print("-----------------")
de_today = datetime.datetime.today()
de_now = datetime.datetime.now()
de_utcnows = datetime.datetime.utcnow()
print(de_today)
print(de_now)
print(de_utcnows)


# using pytz

import pytz

dtp=datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dtp)
de_nowp = datetime.datetime.now(tz=pytz.UTC)
print(de_nowp)

# tz for all time xone
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
for tz in pytz.all_timezones:
    tzi = dt_utcnow.astimezone(pytz.timezone(tz))
    print(tzi , tz)