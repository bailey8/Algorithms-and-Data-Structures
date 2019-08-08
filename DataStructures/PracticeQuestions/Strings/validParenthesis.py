#if opening brace, add it to stack.
# if closing brace, pop from stack, but check if poped element matches
# When string is passed through, check if stack is empty

def valid(str):
    dic = {")":"(","}":"{"}
    stack = []
    for char in str:
        if char in dic:
            if len(stack) == 0 or stack.pop() != dic[char]:
                return False
        else:
            stack.append(char)
    if len(stack) == 0:      
        return True

print(valid("{}{}()({})((())))"))
