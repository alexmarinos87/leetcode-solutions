class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None  (modify nums1 in-place)

        Idea:
          - Two pointers from the end and one write index.
          - Always place the larger of nums1[i] and nums2[j] at nums1[w].
          - Fill from the right to avoid overwriting unread values.

        Correctness invariant:
          - After each iteration, elements to the right of w are final and sorted.

        Time: O(m + n),  Space: O(1)
        """
        i, j, w = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1

