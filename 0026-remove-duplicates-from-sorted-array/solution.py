class Solution(object):
    def removeDuplicates(self, nums):
        """
        In-place remove duplicates from sorted array `nums`.
        Return the number of unique elements `k`; the first `k` slots
        of `nums` will hold the unique elements in original order.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        int
            Number of unique elements in `nums` (k).
        """
        if not nums:
            return 0

        write = 1                          # next index to write a unique value

        for read in range(1, len(nums)):   # start from the second element
            if nums[read] != nums[read - 1]:  # check for uniqueness
                nums[write] = nums[read]      # place the unique value
                write += 1                    # advance write pointer

        return write                         # k = count of unique elements

