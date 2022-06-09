class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0 #beginng of index
        r = len(numbers) - 1 #last index of last elment
        while l < r:
            temp_sum = numbers[l] + numbers[r] #add
            if temp_sum > target: #when the temp sum is too larget, decrease the right index 
                r -= 1
            elif temp_sum < target: #when it is too small, increase the index on the left
                l += 1
            else:
                return [l+1,r+1]
            
        return []