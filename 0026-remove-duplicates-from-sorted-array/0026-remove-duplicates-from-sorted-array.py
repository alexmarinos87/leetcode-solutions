class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        w = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[w-1]:
                nums[w] = nums[r]
                w += 1
        return w