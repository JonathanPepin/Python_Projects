"""
Problem - Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
Input - # of decimal places
Output - e up decimal places specified
Positive test cases - all valid inputs
Negative test cases - one under min, one over max, non-valid input (fails on letters)
"""

from math import e

stringe = str(e)
decPlaces = 0 
while (decPlaces < 1) or (decPlaces > (len(stringe))-2):
    decPlaces = int(input("Enter the number of decimal places you want to generate PI up to between 1 and " + str((len(stringe))-2) + " : "))
print (stringe[0:decPlaces+2])
