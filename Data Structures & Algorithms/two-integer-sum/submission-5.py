class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i,j in enumerate(nums):
            diff = target - j
            if diff in freq:
                return [freq[diff],i]
            freq[j] = i
         