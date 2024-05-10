class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = int(len(nums) // 2)
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] > target:
                return i