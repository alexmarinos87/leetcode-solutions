class Solution(object):
    def summaryRanges(self, nums):
        """
        Approach: Sweep once. Start a range at `start`, extend while next is prev+1.
        On a gap, flush the current range and start a new one.
        """
        res = []
        if not nums:
            return res

        start = prev = nums[0]
        for x in nums[1:]:
            if x == prev + 1:
                prev = x
            else:
                res.append(str(start) if start == prev else "{}->{}".format(start, prev))
                start = prev = x
        res.append(str(start) if start == prev else "{}->{}".format(start, prev))
        return res

