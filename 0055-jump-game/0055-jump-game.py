class Solution(object):
    def canJump(self, nums):
        """
        Determine if you can reach the last index from the first index
        given each number represents your maximum jump length.

        Greedy strategy: Track the furthest index you can reach
        as you iterate through the array.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        bool
            True if reachable, otherwise False.
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False  # Can't reach this index
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True  # Can reach or surpass the last index

        return True
