class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        r = s % k
        return 0 if r == 0 else r
