class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Approach: Sort the array, fix one number, and use two pointers to find the other two.
        Why it fits: Sorting allows us to skip duplicates and use two-pointer traversal efficiently.
        Invariants: For each i, l > i and r starts at the end. Skip duplicates for i, l, and r.
        Correctness: Every unique triplet is considered exactly once due to sorting and deduplication.
        Complexity: Time O(n^2), Space O(1) extra (excluding output), where n = len(nums).
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):  # i fixes the first number; we need at least two more to form a triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate values for the fixed number

            l, r = i + 1, n - 1  # initialize two pointers

            while l < r:
                s = nums[i] + nums[l] + nums[r]  # sum of the triplet

                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])  # valid triplet found

                    # skip duplicates for the left and right pointers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # move both pointers inward to continue searching
                    l += 1
                    r -= 1

                elif s < 0:
                    l += 1  # sum too small; move left pointer right to increase total
                else:
                    r -= 1  # sum too large; move right pointer left to decrease total

        return res

