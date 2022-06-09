class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        #dictionary for roman numerals
        dict1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,  
            "M": 1000
        }
        
        dict2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        

        rom = ""
        i = 0
        #loops when there is an element in the string
        while i < len(s):
            temp = i + 1
            if temp < len(s):
                rom = s[i] + s[temp]
            else:
                rom = s[i]
            if rom in dict2.keys():
                num += dict2.get(rom)
                i += 2
            else:
                num += dict1.get(s[i])     
                i += 1
        return num