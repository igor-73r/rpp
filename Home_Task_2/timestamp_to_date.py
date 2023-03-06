def timestamp_to_date(timestamp, gmt=0):
    def is_leap(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    in_minute = 60
    in_hour = in_minute * 60
    in_day = in_hour * 24
    in_year = 365 * in_day

    if gmt > 0:
        timestamp += gmt * in_hour

    year = 1970
    month = 1
    month_days = [31, 28 + (1 if is_leap(year) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while timestamp >= in_year:
        in_year = in_day * 366 if is_leap(year) else in_day * 365
        timestamp -= in_year
        year += 1

    while timestamp > month_days[month - 1] * in_day:
        timestamp -= month_days[month - 1] * in_day
        month += 1

    day = timestamp // in_day + 1
    hour = (timestamp % in_day) // in_hour
    minute = (timestamp % in_hour) // in_minute
    timestamp %= in_minute

    res = (year, month, day, hour, minute, timestamp)

    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*res)


if __name__ == '__main__':
    check = int(input("Введите значение: "))
    print(timestamp_to_date(check, gmt=4))
