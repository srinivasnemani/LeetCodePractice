class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        insertion_ptr = len(nums1) - 1
        m = m - 1
        while m >= 0 and nums2:
            if nums2[-1] > nums1[m]:
                nums1[insertion_ptr] = nums2.pop()
            else:
                nums1[insertion_ptr] = nums1[m]
                m = m - 1

            insertion_ptr = insertion_ptr - 1

        if nums2:
            nums1[0:insertion_ptr + 1] = nums2        
        
        print(nums1)
        return nums1
