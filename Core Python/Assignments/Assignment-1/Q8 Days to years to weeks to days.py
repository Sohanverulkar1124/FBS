Days = int (input('Days = '))

years = Days // 365 

remainder_Days = Days % 365

weeks = remainder_Days // 7

remainder_weeks_Days = remainder_Days % 7 

print(f'Days to years =' , years, 'remainder Days =',remainder_Days)
print(f'remainder Days to weeks = ',weeks, 'remainder_weeks_days')