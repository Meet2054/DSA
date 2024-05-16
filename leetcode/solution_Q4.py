class Solution:
   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)  # Merge and sort the lists
        n = len(merged_list)
        if n % 2 == 0:
            # If the length is even, median is the average of the middle two elements
            med = (merged_list[n // 2 - 1] + merged_list[n // 2]) / 2
        else:
            # If the length is odd, median is the middle element
            med = merged_list[n // 2]
        return med