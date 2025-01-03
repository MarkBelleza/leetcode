class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = len(nums1) + len(nums2)
        num2 = 0
        even = False
        if num % 2 == 0:
            num = num // 2
            num2 = num - 1
            even = True
        else:
            num = num // 2

        index1 = 0
        index2 = 0
        lst = []
        while num > -1:
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] <= nums2[index2]:
                    lst.append(nums1[index1])
                    index1 += 1
                else:
                    lst.append(nums2[index2])
                    index2 += 1
            elif index1 == len(nums1) and index2 < len(nums2):
                lst.append(nums2[index2])
                index2 += 1
            else:
                lst.append(nums1[index1])
                index1 += 1
            num -= 1

        if even:
            return (lst[-1] + lst[len(lst) - 2]) / 2
        else:
            return lst.pop()
        
        # Time: O(n+m)
        # Space: O(n+m)
