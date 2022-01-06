def is_leap(year):
    print("hi")
    leap = False
    if (year % 4 == 0 and year%100 != 0):     #Years 2100 2000 1900 are not leap years!!

        leap = True
    else:
        leap = False


    return leap

year = int(input())
print(is_leap(year))