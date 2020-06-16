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

class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def helper(start, end, string):
            if start >= end:
                return
        
            # swap the first and last element
            string[start], string[end] = string[end], string[start]        

            return helper(start+1, end-1, string)
    
        helper(0, len(s)-1, s)
#recursive way
def recursive(string):
    l = len(string)
    if l < 2:
        return string
    #               RIGHT SIDE OF STRING     LEFT SIDE OF STRING
    return recursive(string[l//2:]) + recursive(string[:l//2])

sol = Solution()
string = list("Racecar")
print(sol.reverseString(string))
print(string)

a = "abc"
print(recursive(a))
b = a[0:1]
print(b,a)
print(reverse(a))

