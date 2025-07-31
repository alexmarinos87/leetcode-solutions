class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1, in-place, so that nums1 becomes
        a single non-decreasing array of length m + n.

        Parameters
        ----------
        nums1 : List[int]
            First array.  Its first m positions hold valid values,
            and its last n positions are free (initially zero).
        m : int
            Number of valid elements in nums1.
        nums2 : List[int]
            Second array, fully valid and already sorted.
        n : int
            Number of elements in nums2.

        Returns
        -------
        None.  `nums1` is modified in place.
        """
        i = m - 1               # last valid index in nums1
        j = n - 1               # last index in nums2
        write = m + n - 1       # write pointer at the very end of nums1

        # Iterate while nums2 still has elements to place
        while j >= 0:
            # Choose the larger of nums1[i] and nums2[j] to write at `write`
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
