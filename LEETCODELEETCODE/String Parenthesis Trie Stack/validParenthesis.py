#if opening brace, add it to stack.
# if closing brace, pop from stack, but check if poped element matches
# When string is passed through, check if stack is empty

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map  = {'(':')','{':'}','[':']'}
        stack = []
         
        for element in s:
            if element in bracket_map:
                stack.append(element)
            else:
                if not stack or bracket_map[stack.pop()] != element:
                    return False
        return not stack
