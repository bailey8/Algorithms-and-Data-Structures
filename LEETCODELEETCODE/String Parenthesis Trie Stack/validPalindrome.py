#Only include alpha numeric characters
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True



a = "hii"
print(list(a)) # [h,i,i]
print(set(a)) # {h,i}

class Solution:
    def isPalindrome(self,s):
        
        def isPalindromeRecursive(i, j):
            
                if i >= j: return True

                if not s[i].isalnum():
                    return isPalindromeRecursive(i + 1, j)

                if not s[j].isalnum():
                    return isPalindromeRecursive(i, j-1)

                if s[i].lower() != s[j].lower():
                    return False

                return isPalindromeRecursive(i+1, j-1)
            
        left = 0
        right = len(s) - 1

        if left >= right: return True

        return isPalindromeRecursive(left, right)


A = [True, False]
print(any(A))