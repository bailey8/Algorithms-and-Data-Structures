import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, string, k):
        windowSTART = 0
        longestWindow = 0
        seen = collections.defaultdict(int)

        # in the following loop we'll try to extend the range [window_start, window_end]
        for windowEND in range(len(string)):
    
            seen[string[windowEND]] += 1

            # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
            while len(seen) > k:
                left_char = string[windowSTART]
                seen[left_char] -= 1
                if seen[left_char] == 0:
                    del seen[left_char]
                windowSTART += 1  # shrink the window
                # remember the maximum length so far
            longestWindow = max(longestWindow, windowEND-windowSTART + 1)
        return longestWindow