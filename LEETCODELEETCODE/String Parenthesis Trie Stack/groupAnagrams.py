
#Use hashable tuple (can't hash a list)
# O (N Klogk) - loop N times and sort in klogk time
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):

        # SOLUTION SET!!
        ans = defaultdict(list) 

        # ADD EACH ELEMENT TO THE SOLUTION SET
        for s in strs: # N loops

            # THE KEY IS THE SORTED STRING, THE VALUE IS THE NORMAL STRING
            ans[tuple(sorted(s))].append(s) #klogk sort time per element

        return ans.values()

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        
        # FOR EVERY STRING - O(N)
        for s in strs:
            
            count = [0]*26
            
            # FOR EACH CHARACTER IN THE STRING
            for char in s:  #O(K) WHERE K IS NUMBER OF CHARS PER WORD
                
                # BASIC HASHMAP TO TRACK LETTER COUNTS
                count[ord(char) - ord('a')] += 1
            
            # ANY WORD WITH THE SAME LETTER COUNTS IS AN ANAGRAM
            ans[tuple(count)].append(s)
                
        return ans.values()