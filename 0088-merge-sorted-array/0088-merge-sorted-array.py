class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        Idea:
            - Two pointers from the end and one right index
            - Always place the larger of nums1[i] and nums[j] at nums1[w]
            - Filter from right to avoid overwriting unread values

        Correctness invariant:
            - After each iteration elements from the right of w are final and sorted.

        Time: O(m+n) Space: O(1)
        """
        i, j, w = m - 1, n -1, m + n -1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1