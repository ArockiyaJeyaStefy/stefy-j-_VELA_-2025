#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extracting the hour, minute, and second from the input string
    hour, minute, second = map(int, s[:-2].split(':'))
    am_pm = s[-2:]

    # Checking if the time is in the afternoon (PM) and not 12:00 PM
    if am_pm == 'PM' and hour != 12:
        hour += 12
    # Checking if the time is midnight (12:00 AM)
    elif am_pm == 'AM' and hour == 12:
        hour = 0

    # Formatting the result in 24-hour format
    result = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
    
    return result

# Sample Input
input_time = "07:05:45PM"

# Sample Output
output_time = timeConversion(input_time)
print(output_time)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
