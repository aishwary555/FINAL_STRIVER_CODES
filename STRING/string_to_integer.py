def myAtoi(s):
        
        num = '0123456789'
        res = ""
        for x in s:
            if x == ' ' and len(res) == 0:  # Skip leading spaces
                continue
            if x != ' ' and (x in num or x in "-+") and len(res) == 0:  # Handle first valid character
                res += x
            elif x in num:  # Add subsequent digits
                res += x
            else:  # Stop on any invalid character
                break
        
        if res == "" or res in "-+":  # Handle cases with no valid number
            return 0
        else:
            # Convert to integer and clamp within 32-bit signed integer range
            res_int = int(res)
            if res_int < -(2**31):
                return -(2**31)
            elif res_int > (2**31 - 1):
                return (2**31 - 1)
            else:
                return res_int

s = " -042"
res = myAtoi(s)
print(res)