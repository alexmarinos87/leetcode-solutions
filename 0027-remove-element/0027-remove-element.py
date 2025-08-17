class Solution(object):
    def removeElement(self, nums, val):
        """
        Order doesn't matter. Swap `val` with the last active slot.
        Shrink the active length `n`. Re-check the swapped-in value.
        Returns k = new active length.
        Time O(n), Space O(1)
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # move last active element forward
                n -= 1                 # shrink active range
                # do not i += 1 here; need to re-check nums[i]
            else:
                i += 1
        return n
