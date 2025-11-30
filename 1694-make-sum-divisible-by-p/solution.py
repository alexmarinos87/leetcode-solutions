class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum =  sum(nums)
        need = total_sum % p
        if need == 0:
            return 0 # Already divisble

        prefix = 0
        best = len(nums) # We want the minimum

        # Map remainder to earliest index
        seen = {0: -1} # Before array starts
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
        # We want prefix[l] == (prefix - need +p) % p
            target = (prefix - need) % p

            if target in seen:
                best = min(best, i - seen[target])

            # Store earliest occurence of this prefix remainder
            seen[prefix] = i

        return best if best < len(nums) else -1


