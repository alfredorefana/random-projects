from calendar import *

year = int(input('Enter Year: '))

day_charaters = 2   # characters for days (Mo, TU, etc)
week_rows = 1       # 1 line (row) for each week
month_rows = 8      # 8 lines (rows) for each month
year_columns = 3    # 3 columns for all month of the year
print('Calendar of: ', calendar(year, day_charaters, week_rows, month_rows, year_columns))