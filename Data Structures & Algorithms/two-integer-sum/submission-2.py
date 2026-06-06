class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashset:
                return [hashset[complement], index]
            hashset[num] = index