import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Multiply each stone by -1 so we can apply a min-heap, which acts as a max-heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest)
        
        if len(stones) == 1:
            return -stones[0] #negate the -1
        return 0

        # Time: O(N(logN))
        # Space: O(1)

        # Time is N(LogN) since we are inside the loop approciamately N times, and heappush/heappop are logN time
