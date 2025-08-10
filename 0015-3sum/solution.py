class Solution(object):
    def threeSum(self, nums):
        """
        Find all unique triplets that sum to zero (3Sum).

        Approach
        --------
        - Sort the array to enable two-pointer scanning and easy duplicate handling.
        - Fix an anchor at index `i`, then use two pointers `l` and `r` to find pairs
          such that nums[i] + nums[l] + nums[r] == 0.
        - Skip duplicate anchors, and after recording a valid triplet, advance `l` and `r`
          past duplicates so each triplet appears only once.
        - Early stop: if nums[i] > 0 (with the array sorted), no further triplets can sum to zero.

        Parameters
        ----------
        nums : List[int]
            Integers (may include negatives, zeros, and positives).

        Returns
        -------
        List[List[int]]
            All distinct triplets [a, b, c] with a + b + c == 0, in any order.
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Since array is sorted, if anchor > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # Move past duplicates for l and r
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

