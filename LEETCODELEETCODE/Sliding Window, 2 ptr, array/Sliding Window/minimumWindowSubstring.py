# from collections import Counter,defaultdict
# class Solution(object):
#     def minWindow(self,string, t):
        
#         # The characters a satisfiable window must cover mapped to their frequency
#         requiredCharacters = Counter(t)
#         # For our window. Map all characters in the window to their occurrence count. You
#         # will see how we use this below.
#         windowCharacterMapping = Counter()

#         # 2 pointers. Left holds the left index of the window we are inspecting and right
#         # holds the right index.
#         # The approach is simple. We keep moving right (don't touch left) until the window
#         # we hold satisfies all required characters. Then we take note whether the window
#         # we see beats the smallest satisfiable window we have found so far.
#         # We then contract the left pointer in while the window still satisfies all required
#         # characters (at every point continuing to check if we have beaten the smallest window
#         # ever seen to this point)
#         # As soon as the window no longer satisfies, go back to expanding the right pointer.
#         # We are finished when the right pointer runs over the array because we can't keep
#         # expanding the window to satisfy at that point.

#         left = 0
#         right = 0

#         # 'totalCharFrequenciesToMatch' is the total characters we need to match frequency for
#         # in the window. If I have 1 'a' in my window and I need 2 'a' chars...then the char
#         # frequencies don't match.
#         # 'windowMatches' is the count of frequencies that we have satisfied.
#         # When 'totalCharFrequenciesToMatch' == 'windowMatches' then it can be
#         # said that the current window satisfies that property of having all characters with matching
#         # counts to the string t.

#         totalCharFrequenciesToMatch = len(requiredCharacters)
#         windowMatches = 0

#         # We will keep track of the best window we have seen so far
#         minWindowLengthSeenSoFar = float('inf')
#         minWindow = ""
#         while right < len(string):
#             #   Add the character on the right pointer to the hashtable that maps the characters seen
#             #   in the window to their occurrence count
#             characterAtRightPointer = string[right]
#             # We add the frequencies to a SEPERATE STRUCTURE
#             windowCharacterMapping[characterAtRightPointer] +=1
#             #   Is this character part of the requirement
#             rightCharIsARequirement = characterAtRightPointer in requiredCharacters
#             if rightCharIsARequirement:
#                 # Does the current window frequency match the required frequency?
#                 requirementForCharacterMet = requiredCharacters[characterAtRightPointer] == windowCharacterMapping[characterAtRightPointer]
#                 if requirementForCharacterMet:
#                     #   If so then we have one more frequency requirement that matches...remember when:
#                     #   'totalCharFrequenciesToMatch' == 'windowMatches' then we know that
#                     #   we have a satisfying window
#                     windowMatches +=1

#             #   Does this window satisfy? Ok...if it does try contracting the left pointer inward until
#             #   we go over the right pointer.

#             while windowMatches == totalCharFrequenciesToMatch and left <= right:
#                 characterAtLeftPointer = string[left]
#                 windowSize = right - left + 1
#                 # Have we beat the best satisfiable window seen so far? Ok...if so then update
#                 # the tracking variables
#                 if windowSize < minWindowLengthSeenSoFar:
#                     minWindowLengthSeenSoFar = windowSize
#                     minWindow = string[left:right + 1]

#                 # This character will get contracted out. It won't be in the window anymore once
#                 # left moves forward.
#                 windowCharacterMapping[characterAtLeftPointer] -= 1
#                 # Was this character part of the requirement? If so then its frequency changing matters to us.
#                 leftCharIsARequirement = characterAtLeftPointer in requiredCharacters
#                 if leftCharIsARequirement:
#                     # Does the character frequence count not fall below the threshold of satisfying?
#                     characterFailsRequirement = windowCharacterMapping[characterAtLeftPointer] < requiredCharacters[characterAtLeftPointer]
#                     if characterFailsRequirement:
#                         # If so then we have one less character frequency mapping in the window that matches
#                         windowMatches -= 1
#                 # Move the left point forward. We will keep going until the window no longer satisfies.
#                 left +=1
#             # We have moved left as far as it could go. It either led to a window that no longer
#             # satisfied or left passed the right pointer. Either way...advance the right pointer.
#             right +=1

#         return minWindow





# from collections import Counter,defaultdict
# class Solution2(object):
#     def minWindow(self,string, t):
        
#         # The characters a satisfiable window must cover mapped to their frequency
#         requiredCharacters = Counter(t)
#         windowCharacterMapping = Counter()
#         windowSTART = 0

#         totalCharFrequenciesToMatch = len(requiredCharacters)
        
#         windowMatches = 0

#         # We will keep track of the best window we have seen so far
#         minWindowLengthSeenSoFar = float('inf')
#         minWindow = ""
#         for windowEND in range(len(string)):
            
#             rightChar = string[windowEND]

#             # We add the frequencies to a SEPERATE STRUCTURE
#             windowCharacterMapping[rightChar] +=1

#             # Is this character part of the requirement
#             if rightChar in requiredCharacters:

#                 # Does the current window frequency match the required frequency?
#                 if requiredCharacters[rightChar] == windowCharacterMapping[rightChar]: windowMatches +=1

#             #   Does this window satisfy? Ok...if it does try contracting the left pointer inward until we go over the right pointer.

#             while windowMatches == totalCharFrequenciesToMatch and windowSTART <= windowEND:

#                 leftChar = string[windowSTART]
#                 windowSize = windowEND - windowSTART + 1
#                 # Have we beat the best satisfiable window seen so far? Ok...if so then update the tracking variables
#                 if windowSize < minWindowLengthSeenSoFar:
#                     minWindowLengthSeenSoFar = windowSize
#                     minWindow = string[windowSTART:windowEND + 1]

#                 # This character will get contracted out. It won't be in the window anymore once
#                 # windowSTART moves forward.
#                 windowCharacterMapping[leftChar] -= 1
#                 # Was this character part of the requirement? If so then its frequency changing matters to us.
#                 leftCharIsARequirement = leftChar in requiredCharacters
#                 if leftCharIsARequirement:
#                     # Does the character frequence count not fall below the threshold of satisfying?
#                     characterFailsRequirement = windowCharacterMapping[leftChar] < requiredCharacters[leftChar]
#                     if characterFailsRequirement:
#                         # If so then we have one less character frequency mapping in the window that matches
#                         windowMatches -= 1
#                 # Move the left point forward. We will keep going until the window no longer satisfies.
#                 windowSTART +=1
 
#         return minWindow





from collections import Counter,defaultdict
class Solution(object):
    def minWindow(self,string, t):
        
        # The characters a satisfiable window must cover mapped to their frequency
        requiredCharacters = Counter(t)
        windowSTART = 0        
        windowMatches = 0

        minWindow = ""
        
        for windowEND in range(len(string)):
            
            rightChar = string[windowEND]

           
            # Is this character part of the requirement
            if rightChar in requiredCharacters:

                 # We add the frequencies to a SEPERATE STRUCTURE
                requiredCharacters[rightChar] -=1

                # Does the current window frequency match the required frequency?
                if requiredCharacters[rightChar] == 0: windowMatches +=1

            # Does this window satisfy? Ok...if it does try contracting the left pointer inward until we go over the right pointer.
            while windowMatches == len(requiredCharacters):

                leftChar = string[windowSTART]
              
                # UPDATE SMALLEST WINDOW SIZE
                if not minWindow or (windowEND - windowSTART + 1) < len(minWindow):
                    minWindow = string[windowSTART:windowEND + 1]
                
                # Was this character part of the requirement? If so then its frequency changing matters to us.
                if leftChar in requiredCharacters:
                    
                    # Does the character frequence count not fall below the threshold of satisfying?
                    if requiredCharacters[leftChar] == 0:
                        # If so then we have one less character frequency mapping in the window that matches
                        windowMatches -= 1
                        
                    requiredCharacters[leftChar] += 1
                # Move the left point forward. We will keep going until the window no longer satisfies.
                windowSTART +=1
 
        return minWindow

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        chars = collections.Counter(t)
        windowSTART = 0
        smallestWindow = ""
        matches = 0
        
        for windowEND in range(len(s)):
            
            rightChar = s[windowEND]
            
            if rightChar in chars:
                chars[rightChar] -= 1
                if not chars[rightChar]: matches += 1
            
            while matches == len(chars):
                
                if not smallestWindow or len(smallestWindow) > (windowEND - windowSTART + 1):
                    
                    smallestWindow = s[windowSTART: windowEND + 1]
                    
                leftChar = s[windowSTART]
                    
                if leftChar in chars:
                    if chars[leftChar] == 0: matches -= 1

                    chars[leftChar] += 1
                
                windowSTART += 1
                
        return smallestWindow
                
        
            
            
            
        

a = Solution().minWindow("ADOBECODEBANC",
"ABC")

print(a)