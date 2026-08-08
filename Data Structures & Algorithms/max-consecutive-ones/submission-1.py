class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0 

        for n in nums:
            if n == 1:
                count += 1 
            else:
                result = max(result, count)
                count = 0 
    
        return max(result, count)
