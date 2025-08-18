class Solution(object):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        """Time O(N), Space O(U)"""
        def majorityElement(self, nums):
            return Counter(nums).most_common(1)[0][0]