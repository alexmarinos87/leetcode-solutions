class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        Approach: Two pointer (left + right).
        Why it fits: The array is sorted, allowing efficient narrowing by sum comparison.
        Invariants: l < r; the correct pair (if it exists) must lie between these.
        Correctness: At each step, we maintain that target must lie between number[l] + ... + numbers[r]. Moving inward eliminates impossible ranges without missing the correct pair.
        Complexity: Time O(n), Space O(1)
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: 
                return [l + 1, r + 1] # 1-based index
            elif s < target:
                l += 1
            else:
                r -= 1
