from typing import List
class Solution:
    def productOfArrayExceptSelf(self, nums) -> List:
        rp = 1
        n = len(nums)
        result = [0] * n
        result[0] = 1
        # Array containing product to its left
        for i in range(1,n):
            rp *=  nums[i -1]
            result[i] = rp
        rp = 1
        for i in range(n-2, -1,-1):
            rp *= nums[i+1]
            result[i] = result[i] * rp
        return result

s = Solution().productOfArrayExceptSelf([1,2,3,4])
print(s)
