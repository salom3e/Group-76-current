# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. 
# If the array is empty, return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: [-2.398]
# Output: -2.398

# Input: []
# Output: 0

# Assumptions
# You can assume that you are given a (possibly empty) valid array containing only numbers.

def sum_array(nums):
    return sum(nums)


def sum_array(nums):
    if len(nums) > 0:
        return sum(nums)
    else:
        return 0