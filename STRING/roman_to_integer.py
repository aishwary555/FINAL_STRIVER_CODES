def romanToInt(s):
    
        """
        sum = 0
        roman_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        s = s.replace("IV" , "IIII")
        s = s.replace("IX" , "VIIII")
        s = s.replace("XL" , "XXXX")
        s = s.replace("XC" , "LXXXX")
        s = s.replace("CD" , "CCCC")
        s = s.replace("CM" , "DCCCC")

        for char in s:
            sum = sum + roman_to_int[char]
        return sum  
        """

        i = 0
        sum = 0
        roman_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        while i < len(s):
            if( i+1<len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]):
                sum = sum + (roman_to_int[s[i+1]] - roman_to_int[s[i]])
                i = i+2
            else:
                sum = sum + roman_to_int[s[i]]
                i = i+1
        return sum

s = "LVIII"
res = romanToInt(s)
print(res)