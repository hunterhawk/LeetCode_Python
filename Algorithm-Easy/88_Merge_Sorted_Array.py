class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last = last - 1
                i = i - 1
            else:
                nums1[last] = nums2[j]
                last = last - 1
                j = j - 1

        while j >= 0:
            nums1[last] = nums2[j]
            last = last - 1
            j = j - 1

if __name__ == "__main__":
    nums1 = [1, 3, 5, 0, 0, 0, 0]
    nums2 = [2, 4, 6, 7]
    print(Solution().merge(nums1, 3, nums2, 4))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
            Note:
            The number of elements initialized in nums1 and nums2 are m and n respectively.
            You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional
            elements from nums2.

            Example:
            Input:
            nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6],       n = 3
            Output: [1,2,2,3,5,6]
    """