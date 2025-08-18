class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Keep at most two of each value in a sorted array
        Time O(n), Space O(1)
        """
        n = len(nums)
        if n <= 2:
            return n
            
        w = 2 # next write position; first two are always allowed
        for r in range(2, len(nums)):
            if nums[r] != nums[w-2]:
                nums[w] = nums[r]
                w += 1
        return w

        """
        Second solution (this version is more elegant):
        w = 0
        for x in nums:
            if w < 2 or x != numbs[w-2]:
                nums[w] = x
                w += 1
        return w
        """