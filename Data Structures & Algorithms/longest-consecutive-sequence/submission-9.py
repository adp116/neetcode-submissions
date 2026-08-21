class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        numSet = set(nums)
        
        for i in nums:
            if i - 1 not in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                output = max(output,length)
        return output