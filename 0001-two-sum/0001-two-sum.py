class Solution(object):
    def twoSum(self, nums, target):
        """
        Approach: One-pass hash map. For each value x at index i, check if (target-x)
                  has been seen; if yes, return its index with i. Otherwise store x->i.

        Complexity: Time O(n), Space O(n)
        """
        seen = {}  # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
