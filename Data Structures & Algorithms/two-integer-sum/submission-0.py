class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Array = []
        for index, num in enumerate(nums):
            Array.append([num,index])
        
        Array.sort()

        left,right = 0, len(nums) - 1

        while left < right:
            current = Array[left][0] + Array[right][0]
            if current == target:
                return [ min(Array[left][1], Array[right][1]),
                         max(Array[left][1], Array[right][1])]

            elif current < target:
                left += 1
            else:
                right -= 1

        return[]   
