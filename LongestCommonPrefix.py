class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        if len(strs) == 1:
            return strs[0]
        elif len(strs) > 1 and (not ("" in strs)):
            for i in range(len(strs[0])):
                common = common + strs[0][i]
                for j in strs:
                    if j[:i+1] != common:
                        return common[:-1] #do not include the last character in the string
            return common
        else:
            return common

    #Time: O(n * m)
    #Space: O(1)
