try:
  age = int(input("Type your age in years here: "))
  if age > 0:
    age_month = age*12
    age_day = age*365.25
    age_hour = age_day*24
    age_minute = age_hour*60
    age_second = age_minute*60
    print(f"{age} year{'s' if age > 1 else ''} in months is {age_month} \n in days is {age_day:,} \n in hours is {age_hour:,} \n in minutes is {age_minute:,} \n in seconds is {age_second:,}")
  else:
    print("Enter a number greater than 0 Please")
except ValueError:
  print("Enter numbers only")
