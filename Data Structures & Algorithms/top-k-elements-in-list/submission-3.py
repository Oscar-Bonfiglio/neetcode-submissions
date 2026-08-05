class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        arr = []
        for n, total in count.items():
            arr.append([total,n])
        arr.sort()
        
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result

