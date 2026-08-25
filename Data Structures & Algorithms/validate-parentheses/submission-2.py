class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                temp.append(c)
            elif c == ')':
                if len(temp)>0 and temp[len(temp)-1]=='(':
                    temp.remove('(')
                else:
                    return False
            elif c == ']':
                if len(temp)>0 and temp[len(temp)-1]=='[':
                    temp.remove('[')
                else:
                    return False
            elif c == '}':
                if len(temp)>0 and temp[len(temp)-1]=='{':
                    temp.remove('{')
                else:
                    return False
        
        if len(temp)>0:
            return False
        return True
            