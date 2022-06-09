class Solution(object):
    def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            temp_sum = 0
            temp = []
            for x in range(len(nums)):
                for y in range(1, len(nums)):
                    temp_sum = nums[x] + nums[y]
                    if temp_sum == target:
                        temp.append(x)
                        temp.append(y)
                        return temp
                    
            return temp

