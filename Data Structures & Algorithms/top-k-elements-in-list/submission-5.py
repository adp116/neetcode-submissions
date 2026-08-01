class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmp = {}

        for i in nums:
            freqmp[i] = 1 + freqmp.get(i,0)
        
        arr = []
        for num,cnt in freqmp.items():
            arr.append([cnt,num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res 