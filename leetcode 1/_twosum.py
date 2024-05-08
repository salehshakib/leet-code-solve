class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                diff_ind = hashmap[nums[i]]
                return [diff_ind, i]
            else:
                diff = target - nums[i]
                hashmap[diff] = i