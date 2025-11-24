class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        prefix_mod = 0

        for bit in nums:
            prefix_mod = (prefix_mod * 2 + bit) % 5
            ans.append(prefix_mod == 0)
        
        return ans
