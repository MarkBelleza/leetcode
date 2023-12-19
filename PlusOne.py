class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1): #(where to start, where to end {exclusive}, by what incriment/decriment)
            if digits[i] < 9:
                digits[i] += 1
                break
            elif digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            else: digits[i] = 0
        return digits
