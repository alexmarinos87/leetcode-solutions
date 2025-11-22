class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in nums:
            if i % 3 != 0:
                ops += 1
        return ops
