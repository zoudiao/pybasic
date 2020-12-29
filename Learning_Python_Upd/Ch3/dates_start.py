# example file for working with date information

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # get today's date from the simple today() method
    today = date.today()
    print("Today's date is ", today )

    # print out the date's individual components
    print("Date components:", today.day , today.month, today.year)

    # print the weekday
    print("Today's weekday is ",today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("which day is today ? ", days[today.weekday()])

    # today's date from the datetime class
    today = datetime.now()
    print("Today's datetime is ", today)

    # get current time
    t = datetime.time(datetime.now())
    print("The current time is " , t)

if __name__:
    main()