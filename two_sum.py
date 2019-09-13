'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# use hashtable to store values and look up if value and complement match
nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    dict = {}
    for index in nums:
        if 
