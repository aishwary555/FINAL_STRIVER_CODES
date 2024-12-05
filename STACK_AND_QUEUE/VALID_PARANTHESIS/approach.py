def isValid(s):
        st = []
        for i in s:
            if(i =='(' or i == '{' or i =='['):
                st.append(i)
            elif(i == ')' and st and st[-1] == '(' ):
                st.pop()
            elif(i == ']' and st and st[-1] == '[' ):
                st.pop()
            elif(i == '}' and st and st[-1] == '{' ):
                st.pop()
            else:
                return False
        return len(st)==0

res = isValid("(({}[]))")
print(res)