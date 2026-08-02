class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmp = {}

        for i in nums:
            freqmp[i] = 1 + freqmp.get(i,0)
        arr = []
        for num,cnt in freqmp.items():
            arr.append([cnt,num])
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output