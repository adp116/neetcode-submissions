class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            key = i
            if key not in freq:
                freq[key] = 0
            freq[key] += 1

        n = []
        top = sorted(freq, key=freq.get, reverse=True)
        for i in range(k):
            n.append(top[i])
        return n