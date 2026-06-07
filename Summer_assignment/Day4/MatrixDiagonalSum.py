class Solution:
    def diagonalSum(self, mat):

        n = len(mat)
        x = 0
        
        for i in range(n):
            x += mat[i][i]
            x += mat[i][n - 1 - i]
        if n % 2 == 1:
            x -= mat[n // 2][n // 2]    
        return x
