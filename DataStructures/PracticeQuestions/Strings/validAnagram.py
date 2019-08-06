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

# O(1) space complexity, O(n) time complexity -- Only one pass through
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



def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)