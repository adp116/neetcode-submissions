class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMp = {}

        for i in nums:
            if i not in freqMp:
                freqMp[i] = 1
            else:
                freqMp[i] += 1
        n = []
        top = sorted(freqMp, key = freqMp.get, reverse = True)
        for i in range(k):
            n.append(top[i])
        return n 
