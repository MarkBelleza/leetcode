class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not (needle in haystack):
            return -1
        elif len(needle) == 0 or (len(needle) == len(haystack) and needle == haystack):
            return 0
        else: 
            size_needle = len(needle)
            for i in range(len(haystack)):
                if len(haystack) < i + size_needle:
                    break
                else: 
                    if haystack[i:i + size_needle] == needle:
                        return i
            return -1
