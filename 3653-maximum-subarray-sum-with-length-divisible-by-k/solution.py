class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = 0
        best = float('-inf')

        # best_min_prefix[r] = smallest sum prefix seen with index % k = r
        best_min_prefix = [float('inf')] * k
        best_min_prefix[0] = 0 # prefix index = 0, prefix sum = 0

        for i, x in enumerate(nums, start = 1):
            prefix += x
            mod = i % k

            # try using best min prefix[mod] to form a subarray
            best = max(best, prefix - best_min_prefix[mod])

            # update the smallest prefix with this mod class
            best_min_prefix[mod] = min(best_min_prefix[mod], prefix)

        return best

                
