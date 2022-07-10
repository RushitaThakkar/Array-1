class Solution:

    def spiralMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        result = []
        while top <= bottom and left <= right:
            # Left to right
            if top <= bottom:
                for i in range(left, right+1):
                    result.append(mat[top][i])
                top +=1
            
            # Top to Bottom
            if left <= right:
                for j in range(top, bottom+1):
                    result.append(mat[j][right])
                right -=1
            
            # Right to left
            if top <= bottom:
                for k in range(right, left-1, -1):
                    result.append(mat[bottom][k])
                bottom -=1
            
            # bottom to top
            if left <= right:
                for l in range(bottom, top-1, -1):
                    result.append(mat[l][left])
                left +=1
        return result

s = Solution().spiralMatrix([[1,2,3],[4,5,6], [7,8,9]])
print(s)