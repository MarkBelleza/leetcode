class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            tar = numbers[l] + numbers[r]
            if tar == target:
                return [l+1, r+1]
            elif tar < target:
                l += 1
            else:
                r -= 1

    # Time: O(n)
    # Space: O(1)
