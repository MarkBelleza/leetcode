class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left < right):
            while left < right and not s[left].isalnum(): #ignore all non-alphanumerics (alphanumeric includes only numbers and letters)
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
