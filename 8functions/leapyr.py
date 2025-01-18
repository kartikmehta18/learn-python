monthday =[0, 31, 28, 31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)

def dayinmonth(year, month):
    if not 1<= month <=12:
        return "invalid month"
    if month ==2 and is_leap(year):
        return 29
    
    return monthday[month]

print(is_leap(2020))
print(dayinmonth(2020,2))

