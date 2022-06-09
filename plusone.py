class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        largest = []
        
        s = ""
        
        #gets digits and convert to string
        for x in range(len(digits)):
            s += str(digits[x])
        
        #change from string to int then add 1
        
        some_num = int(s)
        some_num += 1
        
        temp = str(some_num)
        for x in range(len(temp)):
            largest.append(temp[x])
        return largest
        