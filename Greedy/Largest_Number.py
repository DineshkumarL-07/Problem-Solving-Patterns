# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
from functools import cmp_to_key

nums = [3,30,34,5,9]
nums = [str(i) for i in nums]

def compareValue(v1,v2):
    if v1 + v2 > v2 + v1:
        return -1
    else:
        return 1
    
nums = sorted(nums, key=cmp_to_key(compareValue))
# the answer has to return in string So, we converting it into string before that we have to convert into integer 
# because we have to handle this case nums = [0,0,0] the output is "0" So that only we are converting it into the integer
print(str(int("".join(nums))))