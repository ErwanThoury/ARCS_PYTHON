def bis(y):
    if y % 4 == 0 and (y % 100 == 0 and y % 400 != 0) != True:
        return 29
    return 28

def daypermonth(m):
    if (m % 2 == 0 and m <= 7) or (m % 2 == 1 and m > 7):
        return 30
    return 31

def daypone(y, m, d):
    daymax = daypermonth(m)

    if m == 2:
        daymax = bis(y)

    if daymax < d or m > 12:
        print("INVALIDE")

    else:
        if d + 1 > daymax:
            if m + 1 > 12:
                print(y+1, 1, 1)
            else:
                print(y, m+1, 1)
        else:
            print(y, m, d+1)

y, m, d = (int(input()),int(input()),int(input()))

daypone(y, m, d)