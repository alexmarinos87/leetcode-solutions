class Solution(object):
    def jump(self, nums):
        """
        Calculate the minimum number of jumps required to reach the last index.

        Greedy approach:
        - At each step, track the farthest you can reach in the current jump range.
        - When you reach the end of the current range, make a jump.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        int
            Minimum number of jumps to reach the last index.
        """
        jumps = 0
        farthest = 0      # The farthest index reachable from current range
        end = 0           # Current jump range end

        for i in range(len(nums) - 1):  # No need to check the last element
            farthest = max(farthest, i + nums[i])

            if i == end:  # Time to jump to the next range
                jumps += 1
                end = farthest

        return jumps
