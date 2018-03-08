#You are given the following information, but you may prefer to do some research for yourself.

#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

t31 = [1, 3, 5, 7, 8, 10, 12] # months with 31 days
t30 = [4, 6, 9, 11] # months with 30 days

def dm(m, y): # checking how many days in a month
    if m in t31:
        d = 31
        return d
    elif m in t30:
        d = 30
        return d
    elif m == 2: # decision how many days february has
        if y & 4 == 0:
            d = 29
            return d
        if y % 400 == 0 and y == 2000:
            d = 29
            return d
        else:
            d = 28
            return d

L = {1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thurs', 6:'Fri', 7:'Sat'} # list of days

c = 1 # counter starts at one because boundary condition is monday
t = 0
for y in range(1900, 2001): # range of years
    for m in range(1, 13): # range of months in a year
        fd = dm(m, y)
        for dd in range(1, fd + 1): # going from first to last day of month
            if dd == 1 and L[c] == "Sun": # if month is 1 and its a sunday
                t += 1
            if c >= 7: # keeping counters inside the day parameter 
                c = 0
            c += 1 # increasing day

print(t-2) # 2 sundays at beginning of month in 1900
