
#write a script to display the calendar for a given year and month.
import calendar
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))

cal=calendar.month(year,month)
print(cal)
