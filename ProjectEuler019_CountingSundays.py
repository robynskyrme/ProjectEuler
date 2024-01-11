# 8.3.2023
# Project Euler 19
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Code works (and the answer is correct) but it's getting late; I'll comment it up in the morning

                            # Set class 'date' with simple day/month/year values
class date:
    def __init__(self, d, m, y):

        self.d = d
        self.m = m
        self.y = y

d = date(0,0,0)

                            # 0 = "none" is a minor cheat to get round the headache of zero-indexing
                            # -- NB this might MATTER, later
months = [None,31,28,31,30,31,30,31,31,30,31,30,31]


                            # Method to shift forward one day in time
def one_day_after(d):
    day = d.d
    month = d.m
    year = d.y

                            #
    day = day + 1
                            # If the day counts higher than the current month, roll over to next month and count day from 1 again
    if day > months[month]:
        day = 1
        month = month + 1
                            # If month goes above 12, roll into next year and start with January again
        if month == 13:
            month = 1
            year = year + 1
                            # If the year has changed, update the length of February accordingly
            months[2] = days_in_february(year)

    d.d = day
    d.m = month
    d.y = year

    return d

                            # Assign 28 or 29 days to February, depending on....
def days_in_february(year):
    days = 28
                            # Case for year being a multiple of 4 (leap year)
    if year%4 == 0:
        days = 29
                            # Exception for centuries (not a leap year)
        if year%100 == 0:
            days = 28
                            # Exception for years divisble by 400 (leap year)
        if year%400 == 0:
            days = 29
                            # Done!
    return days



if __name__ == "__main__":
                            # Start counting from the date given by Project Euler problem
    d = date(1,1,1900)
                            # ... which is a Monday:
    dayofweek = 1
                            # Set a counter for Sundays on the first of the month
    tally = 0

                            # Stop counting on Dec 31 2000
    while d.y < 2001:
                            # Sundays are zero, in this scheme; only do this if it's a sunday
        if dayofweek == 0:
            print(str(d.d) + " " + str(d.m) + " " + str(d.y) + " -- SUNDAY")
        d = one_day_after(d)
        dayofweek = dayofweek + 1
        dayofweek = dayofweek%7

                            # Condition to start conuting only from the year 1901
        if d.y > 1900:
                            # Only add to the counter if day is Sunday AND the date is the 1st
            if dayofweek == 0:
                if d.d == 1:
                    tally = tally + 1


                            # Give the answer
    print("In the twentieth century, " + str(tally) + " Sundays fell on the first of the month")