p = int (input('principal of amount:'))
r = int (input('rate of interest:'))
t = int (input('time of years:'))

CI = (p*(1+(r/100))**t)-p 

print( f'compound of interest is {p} amount ,time {t} years and rate of interest {r} % is : {CI} \n ' )