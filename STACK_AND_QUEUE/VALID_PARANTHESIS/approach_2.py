def isValid(s):
    st = []
    for it in s:
        if it == '(' or it == '{' or it == '[':
            st.append(it)
            
        else:
                        
            if len(st) == 0:
                return False
            ch = st[-1]
            
            if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
                st.pop()
            else:
                return False
    return  len(st)==0

s= "((([{{(([(({{{}}}))]))}}])))"
res = isValid(s)
print(res)
