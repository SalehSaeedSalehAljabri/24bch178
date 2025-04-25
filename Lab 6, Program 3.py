from datetime import date
date1 = (1, 1, 2023)
date2 = (10, 1, 2023)
days_between = (date(date2[2], date2[1], date2[0]) - date(date1[2], date1[1], date1[0])).days
print("Days between:", days_between)
