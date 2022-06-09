import re
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #variables
        #st is string in the list of strings named strs
        #lt is the letter index in each string, starts at 0
        
        #alg:
        #outer loop: loops over items in list
        #inner loop: goes through each letter in the item(a string)
        
        
        long_pre = ""  
        pre = "" #variable for the prefix, temp
        for st in range(0 , len(strs[0])): 
            count = 0
            pre += strs[0][st]
            for lt in range(0, len(strs)):#loop to go through list of strings
                #matching = [item for item in strs if pre in item] #old code
                
                #checks if pre is in the string in the list)
                pattern = '^' + pre     
                result = re.match(pattern, strs[lt])
                if result:
                    count += 1 
                lt += 1    
            if (count == len(strs))and (len(pre) > len(long_pre)) :
                long_pre = pre
            
            st += 1 #increment st
            count = 0

        return long_pre
            
