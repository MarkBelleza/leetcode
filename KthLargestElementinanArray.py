import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We will use min-heap to get the Kth largest element. 

        mean_heapK = [] # this will have a max length of k

        for num in nums:
            if len(mean_heapK) < k:
                heapq.heappush(mean_heapK, num)
            else:
                heapq.heappushpop(mean_heapK, num)
        
        return heapq.heappop(mean_heapK)

        # Time: O(N(logk))
        # Space: O(k)

        # Time is N(Logk) since we are inside the loop N times, and heappush/heappushpop are logK time
        # since they are only applied in mean_heapK (mean_heapK will only have max length of K) 
