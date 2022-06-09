class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        med = 0
        #add elements to num1 list
        for x in nums2:
            nums1.append(x)
        
        x = sorted(nums1)
        if len(nums1) % 2 == 0:
            med = ( float(x[(len(nums1)-1)/2]) + float(x[((len(nums1)-1)/2)+1]) )/ 2
        else:
            med = x[(len(nums1)-1)/2]
            
        return med