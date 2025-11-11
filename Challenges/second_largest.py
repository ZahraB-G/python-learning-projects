# Given an array of positive integers arr[], 
# return the second largest element from the array.
# If the second largest element doesn't exist then return -1. 
# Note: The second largest element should not be equal to the 
# largest element. https://www.geeksforgeeks.org/problems/second-largest3735/1
class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        n = len(arr)
        max_num = arr[n-1]
        for i in range(n-1,-1,-1):
            if max_num != arr[i]:
                return arr[i]
        return -1

solution = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(f'The scond largest number in {arr} is {solution.getSecondLargest(arr)}')
arr = [10, 5, 10]
print(f'The scond largest number in {arr} is {solution.getSecondLargest(arr)}')
arr = [10, 10, 10]
print(f'The scond largest number in {arr} is {solution.getSecondLargest(arr)}')