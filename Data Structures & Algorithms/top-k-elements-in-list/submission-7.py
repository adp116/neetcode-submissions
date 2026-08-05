class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = {}
        for i in nums:
            mp[i] = 1 + mp.get(i,0)
        

        arr = []
        for num,cnt in mp.items():
            arr.append([cnt,num])
        arr.sort()
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

        