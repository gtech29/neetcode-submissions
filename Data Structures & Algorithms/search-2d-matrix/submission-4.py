class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = (l+r) // 2
            rows = m // len(matrix[0])
            columns = m % (len(matrix[0]))

            if target > matrix[rows][columns]:
                l = m + 1
            elif target <  matrix[rows][columns]:
                r = m - 1
            else:
                return True
        return False
        
            
