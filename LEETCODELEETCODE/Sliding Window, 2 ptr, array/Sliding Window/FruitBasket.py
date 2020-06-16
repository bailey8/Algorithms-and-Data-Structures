import collections
class Solution(object):
    def totalFruit(self, tree):

        totalSum = windowSTART = 0
        count = collections.defaultdict(int)

        for windowEND, value in enumerate(tree):
            
            count[value] += 1
            
            # WE CAN ONLY HAVE 2 BASKETS
            while len(count) > 2:
                count[tree[windowSTART]] -= 1
                if not count[tree[windowSTART]]: del count[tree[windowSTART]]
                windowSTART += 1
                
            totalSum = max(totalSum, windowEND - windowSTART + 1)
            
        return totalSum