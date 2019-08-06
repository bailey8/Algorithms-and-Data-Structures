#O(1) space complexity
def u(a):
    a = sorted(a)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True

#Best solution
def unique(str):
    count = [0]*256
    for char in str:
        if count[ord(char)] ==1:
            return False
        count[ord(char)] +=1
    return True

