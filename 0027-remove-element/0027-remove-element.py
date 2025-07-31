class Solution(object):
    def removeElement(self, nums, val):
        """
        In-place remove all occurrences of `val` from `nums`.
        Return the new length k; the first k slots of `nums` will hold
        the elements that are not equal to `val` (order can change).

        Parameters
        ----------
        nums : List[int]
        val  : int

        Returns
        -------
        int
            Number of elements different from `val` (k).
        """
        write = 0                          # next index to keep

        for read in range(len(nums)):      # scan every position once
            if nums[read] != val:          # keep this element
                nums[write] = nums[read]   # overwrite (or copy to itself)
                write += 1                 # advance "good" slot

        return write                       # k = count of kept elements
