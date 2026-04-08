# make a program to determine a leap year

def leap_year(year):
    if year%100==0:
        if year%400==0:
            return 'This is a century year'
        else:
            return 'Not a leap year'
    elif year%4==0:
        return 'This is a leap year'
    else:
        return 'Not a leap year'
