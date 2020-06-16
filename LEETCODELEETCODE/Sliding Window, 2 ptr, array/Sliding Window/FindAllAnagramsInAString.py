class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        windowSTART = charsInWindow = matches = 0
        charFreq = collections.Counter(p)
        indices = []
        
        
        for windowEND in range(len(s)):
            
            rightChar = s[windowEND]
            
            # UPDATE THE MATCHES
            if rightChar in charFreq:
                charFreq[rightChar] -= 1
                if charFreq[rightChar] == 0: matches += 1
                    
            # CHECK TO SEE IF WE HAVE A VALID INDEX
            if len(charFreq) == matches: indices.append(windowSTART)
                
            # OUR WINDOW IS TOO BIG, THERE IS NO WAY THE WINDOW IS AN ANAGRAM IF THE
            # WINDOW IS LONGER THAN THE INTENDED ANAGRAM!!!
            if windowEND - windowSTART + 1 == len(p):
                
                leftChar = s[windowSTART]
                
                if leftChar in charFreq:
                    
                    # THIS LINE MUST MUST MUST GO HERE BEFORE YOU INCREMENT THE CHARFREQ
                    if charFreq[leftChar] == 0: matches -= 1
                    charFreq[leftChar] += 1
                        
                windowSTART += 1               
        
        return indices
            
        