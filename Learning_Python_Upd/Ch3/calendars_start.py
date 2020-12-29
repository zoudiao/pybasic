import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2021,1,0,0)
print(st)


# create an html formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st2 = hc.formatmonth(2021,1)
print(st2)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2020,12):
    print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# calculate days based on a rule: for example, consider a team meeting on the first Friday of every month
# to figure out what days that would be for each month, we can use this script
print("Team meetings will be on:")
for m in range(1,13):
    cal = calendar.monthcalendar(2021,m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.WEDNESDAY] !=0:
        meetday = weekone[calendar.WEDNESDAY]
    else:
        meetday = weektwo[calendar.WEDNESDAY]
    print("%10s %2d" % (calendar.month_name[m],meetday))