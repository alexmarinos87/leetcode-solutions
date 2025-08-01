class Solution(object):
    def removeDuplicates(self, nums):
        """
        In-place remove duplicates from sorted array `nums`, allowing
        at most two occurrences of each unique element.
        Return the new length `k`; the first `k` slots of `nums` will
        contain the result in-place, preserving original order.

        Parameters
        ----------
        nums : List[int]

        Returns
        -------
        int
            Number of elements in the modified array with at most
            two occurrences of each number.
        """
        if len(nums) <= 2:
            return len(nums)  # Already satisfies the condition

        write = 2                          # Start writing from index 2

        for read in range(2, len(nums)):
            # Compare with the element two positions before
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]  # Copy valid value
                write += 1                # Move write pointer

        return write                      # k = count of allowed elements

