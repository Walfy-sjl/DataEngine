import datetime


# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)

def getYearQuarter(year, month):
    list = []
    nn = month // 3
    n = 4
    while n > 0:
        list.append(str(year) + " Q" + str(nn))
        nn = nn - 1
        if nn == 0:
            nn = 4
            year = year - 1
        n = n - 1
    return list


def getYearMonth(year,month):
    list = []
    mm = '{:0>2d}'.format(month)
    yy = year
    if (month-1) == 0:
        mm_last = 12
        yy_last = year-1
    else:
        mm_last = '{:0>2d}'.format(month-1)
        yy_last = year
    list.append(str(yy_last) + "-" + str(mm_last))
    list.append(str(yy) + "-" + str(mm))
    return list


list = getYearMonth(2020,5)
print(list)

# d = datetime.date.today()
# print('{:02d}'.format(d.month))
