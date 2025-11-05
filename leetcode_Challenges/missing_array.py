# Credit: This is inspired by a coding exercise  from GeeksforGeeks.
# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/a
# You are given an array arr[] of size n - 1 
# that contains distinct integers in the range 
# from 1 to n (inclusive). 
# This array represents a permutation of the 
# integers from 1 to n with one element missing. 
# Your task is to identify and return the missing element.
class Solution:
    def missingNum(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(0,n):
            if arr[i] != i+1:
                return(i+1)
        else: return (n+1)
solution = Solution()
arr = [1, 2, 3, 5]
print(f'The missing value of this array {arr} is {solution.missingNum(arr)}')
arr = [8, 2, 4, 5, 3, 7, 1]
print(f'The missing value of this array {arr} is {solution.missingNum(arr)}')
arr = [1]
print(f'The missing value of this array {arr} is {solution.missingNum(arr)}')