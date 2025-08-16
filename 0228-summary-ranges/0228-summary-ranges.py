class Solution(object):
    def summaryRanges(self, nums):
        """
        Summary Ranges (LeetCode 228)

        Approach
        --------
        Single pass (O(n)):
        - Track the start of the current consecutive run.
        - When the run breaks, emit "start->prev" or "start" if length 1.
        - Flush the final run at the end.

        Parameters
        ----------
        nums : List[int]
            Sorted array of unique integers.

        Returns
        -------
        List[str]
            Minimal list of ranges covering all numbers exactly.
        """
        res = []
        if not nums:
            return res

        start = prev = nums[0]
        for x in nums[1:]:
            if x == prev + 1:
                prev = x
            else:
                if start == prev:
                    res.append(str(start))
                else:
                    res.append("{}->{}".format(start, prev))
                start = prev = x

        # flush the last range
        if start == prev:
            res.append(str(start))
        else:
            res.append("{}->{}".format(start, prev))

        return res

