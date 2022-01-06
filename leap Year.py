def is_leap(year):
    leap = False
    if (year % 4 == 0):     #Years 2100 2000 1900 are not leap years!!
        if(year % 400 == 0)
            leap = True
        else:
            leap= False
    else:
        leap = False


    return leap


year = int(input())
print(is_leap(year))