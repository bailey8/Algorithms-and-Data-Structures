class Solution:
    def lengthOfLongestSubstring(self, s):
        slow_pointer, fast_pointer = 0,0
        maxSize = 0

        #USED TO HOLD ALL THE UNIQUE CHARACTERS IN THE WINDOW
        characters = set()

        # OUR FAST POINTER WILL GET TO THE END FIRST
        while fast_pointer < len(s):

            # IF THE ELEMENT IS NOT IN THE SET, THEN ADD IT TO THE SET
            # IF ITS NOT IN SET, WE KNOW OUR MAX SUBSTRING HAS INCREASES BY 1
            if s[fast_pointer] not in characters:
                characters.add(s[fast_pointer])
                fast_pointer += 1

                # UPDATE MAX AFTER EACH ITERATION WHEN WE FIND A NEW UNIQUE CHARACTER
                maxSize = max(len(characters),maxSize)
            
            # IF THE ELEMENT IS ALREADY IN THE SET THEN WE HAVE TO REMOVE FROM THE BEGINNING
            # REMOVE AN OLD CHARACTER
            else:

                # NO NEED TO UPDATE MAX HERE, REMOVING A LETTER FROM SET WILL NEVER UPDATE MAX
                #IT JUST DELETES THE DUPLICATE CHARACTER WE WERE STUCK ON SO WE CAN KEEP EXPLORING FORWARD
                characters.remove(s[slow_pointer])
                slow_pointer += 1

        return maxSize


class Solution:
    def lengthOfLongestSubstring(self, s):
    
        if len(s) == 0: return 0
        previous_position = {}
        maximum = 0
        beginningOfWindow = 0
        
        for endOfWindow in range(len(s)):

            # IF THE CHARACTER IS IN THE DICTIONARY THEN THIS SUBSET IS OVER
            if s[endOfWindow] in previous_position:
                #THE SECOND POINTER MOVES FORWARD (as long as its not already ahead of the character which is what the max checks for)
                beginningOfWindow = max(beginningOfWindow,previous_position[s[endOfWindow]] +1)
            
            # NOW THAT WE SAW THE CHARACTER AGAIN, WE UPDATE ITS "LAST SEEN"
            # POSITION TO THE POSITION WE ARE AT NOW!
            previous_position[s[endOfWindow]] = endOfWindow

            # compare your new window to the old window
            maximum = max(maximum,endOfWindow-beginningOfWindow+1)
        
        return maximum
    

# THE GOOD WAY
class Solution:
    def lengthOfLongestSubstring(self, s):
    
        windowSTART = longest = 0
        visited = set()
        
        for windowEND in range(len(s)):
            
            rightChar = s[windowEND]
            
            # REMOVE ALL CONFLICTING LETTERS
            while rightChar in visited:
                
                leftChar = s[windowSTART]
                visited.remove(leftChar)
                windowSTART += 1
                
            visited.add(rightChar)
            
            longest = max(longest, windowEND - windowSTART + 1)
            
        return longest
                
                
                
            