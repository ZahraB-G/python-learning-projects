# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice. You can return the answer in any order.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in nums[i+1:]:
                result.append(nums.index(goal,i+1))
                result.append(i)
        result.sort()     
        return result
