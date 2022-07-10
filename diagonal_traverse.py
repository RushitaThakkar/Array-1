class Solution:
    def diagonalTraverse(self, mat):
        m = len(mat)
        n = len(mat[0])
        index = 0
        direction = 1
        r = 0
        c = 0
        result = [0]*(m*n)

        while index < m*n:
            result[index] = mat[r][c]
            
            if direction == 1:
                if c == n-1:
                    direction = -1
                    r += 1
                elif r == 0:
                    direction = -1
                    c += 1
                else:
                    r -=1
                    c += 1
            
            else:
                
                if r == m-1:
                    direction = 1
                    c +=1
                elif c == 0:
                    direction = 1
                    r +=1
                else:
                    r += 1
                    c -= 1
            index += 1

        return result
s = Solution().diagonalTraverse([[1,2,3], [4,5,6], [7,8,9]])
print(s)


