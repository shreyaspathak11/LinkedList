def is_leap(year):
    leap = False
    if(year%4==0):
        leap = True
    else :
        leap = False
    # Write your logic here

    print(leap)


year = int(input())
is_leap(year)

