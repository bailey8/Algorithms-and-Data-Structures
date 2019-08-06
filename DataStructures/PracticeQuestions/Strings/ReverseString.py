def reverseString(self, s):
    return s[::-1]

#Iterative way
def reverse(str):
    arr = list(str)
    i = 0
    j = len(arr) -1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -=1
    return "".join(arr)

#recursive way
def recursive(str):
    l = len(str)
    if l < 2:
        return str
    return recursive(str[l//2:]) + recursive(str[:l//2])

a = "abc"
print(recursive(a))
b = a[0:1]
print(b,a)
print(reverse(a))

