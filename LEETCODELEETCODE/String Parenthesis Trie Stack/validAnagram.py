def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


def isAnagram2(self, s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2

# 4 PASSES (ONE IN EACH STRING AND OVER ARRAY AND BUILDING ARRAY)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0]*26
        
        for char in s:
            array[ord(char) - ord('a')] += 1
        for char in t:
            array[ord(char) - ord('a')] -=1
            
        for num in array:
            if num: return False
        return True
        

# O(1) space complexity, O(n) time complexity -- Only 3 TOTAL PASSES THOUGH
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    dic = [0] * 26
    for i in range(len(s)):
        dic[ord(s[i]) - ord('a')] += 1
        dic[ord(t[i]) - ord('a')] -= 1
    for i in dic:
        if i != 0:
            return False
    return True


class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        array = [0]*26
        
        if len(s) != len(t): return False
    
        for char1,char2 in zip(s,t):
            array[ord(char1) - ord('a')] += 1
            array[ord(char2) - ord('a')] -=1
            
        for num in array:
            if num: return False
        return True
        

def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)