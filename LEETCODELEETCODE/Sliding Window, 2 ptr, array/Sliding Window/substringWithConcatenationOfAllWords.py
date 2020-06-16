class Solution:
    def findSubstring(self, s: str, words):
        
        
        def dfs(index, visited):
            
            if len(visited) == len(words): return True
            
            for i,word in enumerate(words):
                if i not in visited:
                    sub = s[index:index + len(word)]
                    if sub == word:
                        visited.add(i)
                        if dfs(index+len(word),visited): return True
                        visited.remove(i)
                        
            return False
        
        answer = []
        totalSize = len(list("".join(words)))
        for i in range(len(s)):
            if dfs(i, set()): answer.append(i)
        
        return answer
        

a = Solution().findSubstring("barfoothefoobarman", ["foo","bar"])

    
import collections

class Solution:
    def findSubstring(self, str, words):
        
        if not words or not str: return []

        word_frequency = collections.Counter(words)

        result_indices = []
        word_length = len(words[0])

        for windowSTART in range((len(str) - len(words) * word_length)+1):

            #RESET THE WORDS SEEN EACH ITERATION
            words_seen = collections.defaultdict(int)

            # CHECK EVERY WORD
            for wordIndex in range(len(words)):
                
                # THIS IS THE NEXT "START" INDEX FOR US TO CHECK
                windowEND = windowSTART + (wordIndex * word_length)

                # Get the next word from the string
                word = str[windowEND: windowEND + word_length]

                if word not in word_frequency:  break

                # Add the word to the 'words_seen' map
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency[word]: break

                if wordIndex + 1 == len(words):  result_indices.append(windowSTART)

        return result_indices



 
import collections

class Solution:
    def findSubstring(self, s, words):
        
        if not words or not s: return []
        wordLength = len(words[0])
        wordSet = collections.Counter(words)
        starts = []
        
        
        # Iterate through every start index
        for startINDEX in range(len(s) - (len(words) * wordLength) + 1):
            
            seen = collections.defaultdict(int)
            visited = set()
            
            # Skip "wordChunkSize" Each iteration
            for wordChunkStart in range(startINDEX, len(s), wordLength):
                
                # This is the substring we are trying to match
                sub = s[wordChunkStart:wordChunkStart + wordLength]
                
                # Only consider the word if it is valid
                if sub in wordSet and sub not in visited:
                    seen[sub] += 1
                    if seen[sub] == wordSet[sub]: visited.add(sub)
                    
                    if len(visited) == len(wordSet): starts.append(startINDEX)
                
                # If we couldn't use the word then we are done for this iteration
                else:
                    break
    
        return starts
                
                                
            
            
            
    
    