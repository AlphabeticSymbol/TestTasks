from datetime import datetime as d
from math import fabs as f

date1 = '1/1/2020'
date2 = '10/1/2020'

def date_difference(d1, d2):
    d1 = d.strptime(d1, '%d/%m/%Y')
    d2 = d.strptime(d2, '%d/%m/%Y')

    difference = (d2 - d1).days
    print(f(difference))

date_difference(date1, date2)