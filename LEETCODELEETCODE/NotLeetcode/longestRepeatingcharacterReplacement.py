# left, right: two endpoints of our sliding window
# res: longest repeating characters found so far, by using less than or equal to k replacements.
# d: counts of all elements in the current sliding window
# right - left + 1 - max_freq : the remaining elements besides the elements with most counts
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        maxSizeSoFar = 0
        # count for the sliding window
        countInWindow = Counter()
        maxSizeTotal = 0
		
        while right < len(s):
            countInWindow[s[right]] += 1
            # Biggest size will be max between prev biggest and current max window count
            maxSizeTotal = max(maxSizeTotal, countInWindow[s[right]])
            # distance = left - right + 1
            # changesNeeded = distance - maxSizeTotal
            # We have 10 spots, and X of the spots are the same letter, so change the rest
            # If we have too many changes, then this window won't work.x
            while left - right + 1 - maxSizeTotal > k:
                countInWindow[s[left]] -= 1
                left += 1
            maxSizeSoFar = max(maxSizeSoFar, right - left + 1)
            right += 1
        return maxSizeSoFar
        
from collections import Counter
def characterReplacement(self, word, k):
    count = Counter()
    left = result = 0
    for right in range(len(word)):
        currentLetter = word[right]
        count[currentLetter] += 1
        max_count = count.most_common(1)[0][1]
        # if edits we must make is too much, shrink window
        if right - left + 1 - max_count > k:
            count[word[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
 