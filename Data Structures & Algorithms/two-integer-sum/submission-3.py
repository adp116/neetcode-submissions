class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMp = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMp:
                return [prevMp[diff],i]
            else:
                prevMp[n] = i
        