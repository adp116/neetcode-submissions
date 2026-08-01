class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMp = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff not in prevMp:
                prevMp[diff] = i
            else:
                return [prevMp[diff], i]
            prevMp[n] = i