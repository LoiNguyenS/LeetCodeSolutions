class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        
        lst = s.split() #puts into list separated by a space
        st = lst[len(lst)-1].strip() # gets the last word of the list, then gets rid of spaces at the beginning and the end
        num = len(st)
        return  num
    