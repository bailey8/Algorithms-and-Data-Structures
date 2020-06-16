import collections

def length_of_longest_substring(s, k):
    
    windowSTART, longest, totalOccurrencesOfChosenChar = 0, 0, 0
    frequency_map = collections.defaultdict(int)

    # Try to extend the range [window_start, window_end]
    for windowEND in range(len(s)):

        rightChar = s[windowEND]
        frequency_map[rightChar] += 1


        totalOccurrencesOfChosenChar = max(totalOccurrencesOfChosenChar, frequency_map[rightChar])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (windowEND - windowSTART + 1 - totalOccurrencesOfChosenChar) == k + 1:
            leftChar = s[windowSTART]
            frequency_map[leftChar] -= 1
            windowSTART += 1

        longest = max(longest, windowEND - windowSTART + 1)
    return longest


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
