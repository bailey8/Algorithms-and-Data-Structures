def repeat(str):
    char = [0] * 256
    for i in str:
        char[ord(i)] +=1
        if char[ord(i)] > 1:
            return i
    return None

print(repeat("abcc"))
print(repeat("aabc"))
print(repeat("abc"))
print(repeat("abbbbbcc"))