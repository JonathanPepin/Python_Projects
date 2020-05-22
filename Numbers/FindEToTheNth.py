"""
Problem - Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
Input - # of decimal places
Output - e up decimal places specified
Positive test cases - all valid inputs
Negative test cases - one under min, one over max, non-valid input (fails on letters)
"""

from decimal import Decimal, getcontext


decPlaces = 0 
maxDecPlaces = 10000
while (decPlaces < 1) or (decPlaces > maxDecPlaces):
    decPlaces = int(input("Enter the number of decimal places you want to generate e up to between 1 and " + str(maxDecPlaces) + " : "))

# Calculating e
getcontext().prec = decPlaces + 1 # set the precision

e = Decimal(0)
f = Decimal(1)
i = Decimal(1)

while (True):
    olde = e
    e += Decimal(1) / f
    if (e == olde):
        break
    f *= i
    i += Decimal(1)  

print(e)