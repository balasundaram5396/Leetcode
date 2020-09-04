# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        
        for i in range(0, len(matrix)):
            matrix[i] = reversed(matrix[i])

    #TC- O(n^2), SC- O(1)