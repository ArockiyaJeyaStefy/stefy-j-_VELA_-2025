#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Check if the length of the string is odd, as anagrams can only be formed with strings of equal length
    if len(s) % 2 != 0:
        return -1

    # Split the string into two substrings
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    # Count the occurrences of each character in both substrings
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Calculate the minimum number of changes needed to make the substrings anagrams
    changes_needed = 0
    for i in range(26):
        changes_needed += abs(count_s1[i] - count_s2[i])

    # The result is half of the changes_needed, as we are counting the changes in both substrings
    return changes_needed // 2

# Sample Input
test_cases = ["aaabbb", "ab", "abc", "mnop", "xyyx", "xaxbbbxx"]

# Sample Output
for test_case in test_cases:
    result = anagram(test_case)
    print(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()