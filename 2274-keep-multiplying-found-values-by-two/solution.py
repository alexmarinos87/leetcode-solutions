class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # convert a set for o(1) membership checks
        s = set(nums)

        # keep doubling as long as the number exists
        while original  in s:
            original = original * 2
        
        # when it is not longer in the set return the original
        return original
