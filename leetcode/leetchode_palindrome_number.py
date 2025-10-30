# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_value = str(x)
        if new_value == new_value[::-1]:
            return True
        else:
            return False