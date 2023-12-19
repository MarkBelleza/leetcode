class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            temp = None
            for i in range(n): #nums2
                for j in range(m): #nums1
                    if nums1[j] > nums2[i]:
                        temp = nums1[j]
                        nums1[j] = nums2[i]
                        nums2[i] = temp
                nums1[m] = nums2[i]
                m += 1
                
        #or
        
        #last_Index = m + n - 1
        #while m > 0 and n > 0:
        #    if nums1[m - 1] > nums2[n - 1]:
        #        nums1[last_Index] = nums1[m - 1]
        #        m -= 1
        #    else:
        #        nums1[last_Index] = nums2[n - 1]
        #        n -= 1
        #    last_Index -= 1
        ##fill the rest of nums1 with the leftovers of nums2, if any
        #while n>0:
        #    nums1[last_Index] = nums2[n - 1]
        #    n -= 1
        #    last_Index -= 1
