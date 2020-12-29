from datetime import datetime

def main():
    now = datetime.now()
    # %y/%Y - year, %a/%A - weekday, %b/%B 0 month , %d 0 day of month
    print(now.strftime("The current year is:%Y"))

    # %c - local's date and time , %x - local's date, %X - locale's time
    print(now.strftime("locale date and time: %c"))
    print(now.strftime("locale date : %x"))
    print(now.strftime("locale time: %X"))

    # %I/%H - 12/24 hour, %M - minutre, %S - second, %p - locale's AM/PM
    print(now.strftime("current time: %I:%M:%S %p"))
    print(now.strftime("current time: %H:%M:%S %p"))

if __name__:
    main()