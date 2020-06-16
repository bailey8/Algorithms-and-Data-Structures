class Solution(object):
    def findLongestChain(self, pairs):
        
        # CURRENT END TIME, TOTAL ITEMS IN OUR CHAIN
        lastEnd, ans = float('-inf'), 0
        
        # ITERATE OVER SORTED INTERVALS BY END TIME
        for start, end in sorted(pairs, key = lambda x: x[1]):
            
            # IF THERE IS NO CONFLICT
            if lastEnd < start:
                #UPDATE THE LAST END TIME
                lastEnd = end
                #ADD 1 TO OUR SOLUTION BC WE SUCCESSFULLY COMPLETED ANOTHER MEETING
                ans += 1
        return ans