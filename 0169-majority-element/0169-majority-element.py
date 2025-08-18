class Solution(object):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        """
        Time O(N), Space O(U)
        I use Python's collections. Counter to count the frequency of each number in the array. Since the majority element is guaranteed to appear more than n//2 times, I can use most_common(1) to directly return the element with the highest count. This solution runs in O(n) time because it makes one pass through the list to build the counter. However, it uses O(u) space, where u is the number of unique elements in the list, so it does not satisfy the follow-up constraint of O(1) space.
        """
        def majorityElement(self, nums):
            return Counter(nums).most_common(1)[0][0]