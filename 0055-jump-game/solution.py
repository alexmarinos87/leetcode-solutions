class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Greedy: Track the furthest index reachable
        Time: O(n), Space: O(1)
        """
        max_reach = 0

        for j in range(len(nums)):
            if j > max_reach:
                return False # can't even get here
            max_reach = max(max_reach, j + nums[j])
            if max_reach >= len(nums) -1:
                return True
        return True
