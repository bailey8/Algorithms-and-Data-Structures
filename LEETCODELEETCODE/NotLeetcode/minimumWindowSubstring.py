 
# Brute Force - search every possible window and see if all characters are in it

def minWindo0w(searchString,t):
    n = len(searchString)
    minWindowLengthSeenSoFar = float('-inf')
    minWindow = ""

    # Explore all left boundaries for windows. AT EACH planting of
    # a left boundary, explore all right boundaries.
    # This is how we explore all windows of substrings we can take.
    for left in range(n):
        for right in range(left,n):
            # Take the snippet that will give us the window we want to
            # investigate. Do 'right + 1' since .substring excludes upper
            # index, so basically we get a snippet from index 'left' ro 'right'
            windowSnippet = searchString[left:right + 1]
            # Test the window
            windowContainsAllChars = stringContainsAllCharacters(windowSnippet, t)

            # If it satisfies and is smaller than the 'minWindowLengthSeenSoFar', update the 'minWindowLengthSeenSoFar' and the minWindow string
        if (windowContainsAllChars and len(windowSnippet) < minWindowLengthSeenSoFar):
            minWindowLengthSeenSoFar = len(windowSnippet)
            minWindow = windowSnippet
    # Return the minWindow. If no window satisfies we will end up returning the "" anyway
    # since that was minWindow's default value and it would never have gotten set
    return minWindow

def stringContainsAllCharacters(searchString, t):

    #  Build a mapping to put all of t's characters inside
    requiredCharacters = Counter(t)
    # Go over the search string and eliminate characters from the hashtable
    for i in range(len(searchString)):
        # Extract the current character
        curChar = searchString[i]
        # Is there a match to the required characters?
        if curChar in requiredCharacters:
            #Calculate what the new occurrence count will be
            newOccurrenceCount = requiredCharacters[curChar] - 1
                # If we have satisfied all of the characters for this character, remove the key from the hashtable.
                # Otherwise, just update the mapping with 1 less occurrence to satisfy for
            if newOccurrenceCount == 0:
                del requiredCharacters[curChar]
            else:
                requiredCharacters[curChar] =  newOccurrenceCount
    # If we satisfied all characters the the required characters hashtable will be empty
    return True if len(requiredCharacters) == 0 else False

# -------------------------------------------------------------------------------------
from collections import Counter
def minWindow(searchString, t):
    # The characters a satisfiable window must cover mapped to their frequency
    requiredCharacters = Counter(t)
    # For our window. Map all characters in the window to their occurrence count. You
    # will see how we use this below.
    windowCharacterMapping = Counter()

    # 2 pointers. Left holds the left index of the window we are inspecting and right
    # holds the right index.
    # The approach is simple. We keep moving right (don't touch left) until the window
    # we hold satisfies all required characters. Then we take note whether the window
    # we see beats the smallest satisfiable window we have found so far.
    # We then contract the left pointer in while the window still satisfies all required
    # characters (at every point continuing to check if we have beaten the smallest window
    # ever seen to this point)
    # As soon as the window no longer satisfies, go back to expanding the right pointer.
    # We are finished when the right pointer runs over the array because we can't keep
    # expanding the window to satisfy at that point.
  
    left = 0
    right = 0

    # 'totalCharFrequenciesToMatch' is the total characters we need to match frequency for
    # in the window. If I have 1 'a' in my window and I need 2 'a' chars...then the char
    # frequencies don't match.
    # 'charFrequenciesInWindowThatMatch' is the count of frequencies that we have satisfied.
    # When 'totalCharFrequenciesToMatch' == 'charFrequenciesInWindowThatMatch' then it can be
    # said that the current window satisfies that property of having all characters with matching
    # counts to the string t.

    totalCharFrequenciesToMatch = len(requiredCharacters)
    charFrequenciesInWindowThatMatch = 0

    # We will keep track of the best window we have seen so far
    minWindowLengthSeenSoFar = float('inf')
    minWindow = ""
    while right < len(searchString):
        #   Add the character on the right pointer to the hashtable that maps the characters seen
        #   in the window to their occurrence count
        characterAtRightPointer = searchString[right]
        # We add the frequencies to a SEPERATE STRUCTURE
        windowCharacterMapping[characterAtRightPointer] +=1
        #   Is this character part of the requirement
        rightCharIsARequirement = characterAtRightPointer in requiredCharacters
        if rightCharIsARequirement:
            # Does the current window frequency match the required frequency?
            requirementForCharacterMet = requiredCharacters[characterAtRightPointer] == windowCharacterMapping[characterAtRightPointer]
            if requirementForCharacterMet:
                #   If so then we have one more frequency requirement that matches...remember when:
                #   'totalCharFrequenciesToMatch' == 'charFrequenciesInWindowThatMatch' then we know that
                #   we have a satisfying window
                charFrequenciesInWindowThatMatch +=1

        #   Does this window satisfy? Ok...if it does try contracting the left pointer inward until
        #   we go over the right pointer.
    
        while charFrequenciesInWindowThatMatch == totalCharFrequenciesToMatch and left <= right:
            characterAtLeftPointer = searchString[left]
            windowSize = right - left + 1
            # Have we beat the best satisfiable window seen so far? Ok...if so then update
            # the tracking variables
            if windowSize < minWindowLengthSeenSoFar:
                minWindowLengthSeenSoFar = windowSize
                minWindow = searchString[left:right + 1]
       
            # This character will get contracted out. It won't be in the window anymore once
            # left moves forward.
            windowCharacterMapping[characterAtLeftPointer] -= 1
            # Was this character part of the requirement? If so then its frequency changing matters to us.
            leftCharIsARequirement = characterAtLeftPointer in requiredCharacters
            if leftCharIsARequirement:
                # Does the character frequence count not fall below the threshold of satisfying?
                characterFailsRequirement = windowCharacterMapping[characterAtLeftPointer] < requiredCharacters[characterAtLeftPointer]
                if characterFailsRequirement:
                    # If so then we have one less character frequency mapping in the window that matches
                    charFrequenciesInWindowThatMatch -= 1
            # Move the left point forward. We will keep going until the window no longer satisfies.
            left +=1
        # We have moved left as far as it could go. It either led to a window that no longer
        # satisfied or left passed the right pointer. Either way...advance the right pointer.
        right +=1
    
    return minWindow
