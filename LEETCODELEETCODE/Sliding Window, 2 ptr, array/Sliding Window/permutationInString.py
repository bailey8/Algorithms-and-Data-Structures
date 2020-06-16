import collections

class Solution:
    def checkInclusion(self, pattern: str, s2: str) -> bool:
        windowSTART, matched = 0, 0
        char_frequency = collections.Counter(pattern)

        # our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for windowEND in range(len(s2)):

            right_char = s2[windowEND]

            if right_char in char_frequency:

                # decrement the frequency of matched character
                char_frequency[right_char] -= 1

                # THIS MEAN WE HAVE SUCCESSFULLY MATCHED ALL OF THIS LETTER
                # IF THE PATTERN HAD 2 'A'S, THEN THIS WOULD MEAN THAT WE HAVE 2 'A'S IN OUR WINDOW
                if char_frequency[right_char] == 0: matched += 1

            if matched == len(char_frequency):
                return True

            # shrink the window by one character because WE WILL DEFINETLY
            # NOT HAVE THE PERMUTATION IN OUR WINDOW IF OUR WINDOW IS LONGER
            # THAN THE PERMUTATION ITSELF
            if windowEND - windowSTART + 1 == len(pattern):
                left_char = s2[windowSTART]
                windowSTART += 1
                
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
        
                    char_frequency[left_char] += 1

        return False
    
       

    
    
       


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()
