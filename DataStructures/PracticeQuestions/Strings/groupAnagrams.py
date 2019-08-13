
#Use hashable tuple (can't hash a list)
# O (N Klogk) - loop N times and sort in klogk time
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

#They are anagrams if count of letters is the same
class Solution2:
    def groupAnagrams(self,strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

dic = {1:"hi"}
print(dic.values())