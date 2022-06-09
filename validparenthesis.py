class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dict1 = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
      
        stack = []
        
        for x in range(len(s)):
            
            if s[x] in ("(","{","["):
                stack.append(s[x]) #push to the stack if it is ( or { or [
            else:
                if stack: #if stack is not empty , you can pop from stack
                    element = stack.pop() 
                # if the element that is popped is not the same as the dictionary, string is not valid
                    if element != dict1[s[x]]: 
                        return False
                else:
                    return False
            
        return not stack #when the stack is empty it is considered false,so not false is true so an empty list would return true