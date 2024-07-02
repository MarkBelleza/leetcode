class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = []

        #Find the correct row to check
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                if matrix[mid][0] == target or matrix[mid][-1] == target:
                    return True
                row = matrix[mid]
                break
            elif matrix[mid][-1] < target: # check right side (bottom part of 2d matrix)
                l =  mid + 1
            else: # check left side (top part of 2d matrix)
                r = mid - 1
        
        if not row:
            return False
        
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (r + l) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target: 
                l = mid + 1 # check right side
            else: 
                r = mid - 1 # check left side
        return False

        #Time: O(log(n)+log(m)) = O(log(n*m)) as the question required
        #Time: O(m) 
