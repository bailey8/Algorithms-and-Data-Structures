chars = 256

#Naive Solution - count is helper function
def count(str):
    count = [0] * chars
    for char in str:
        #ord finds unicode code point
        count[ord(char)] += 1
    return count

def find(string):
    counts = count(string)
    first = None
    for char in string:
        if(counts[ord(char)] ==1):
            first = char
            break
    return first




