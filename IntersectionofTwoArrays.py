class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)

        ans = []
        for num in num1:
            if num in num2:
                ans.append(num)

        return ans

    # Time: O(n + m)
    # Space: O(n + m)
