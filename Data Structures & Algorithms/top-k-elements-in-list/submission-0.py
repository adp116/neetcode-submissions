class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            key = i
            if key not in freq:
                freq[key] = 0
            freq[key] += 1
        top = sorted(freq, key= freq.get, reverse = True)
        n = []
        for i in range(k):
            n.append(top[i])
        return n
            