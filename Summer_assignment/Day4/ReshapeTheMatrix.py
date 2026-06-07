class Solution:
    def matrixReshape(self, mat, r, c):

        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        shape = [num for row in mat for num in row]
        new_matrix = []
        for i in range(r):
            new_matrix.append(shape[i * c : (i + 1) * c]) 
        return new_matrix
