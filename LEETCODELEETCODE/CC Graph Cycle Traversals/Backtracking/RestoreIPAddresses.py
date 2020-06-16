        
            
class Solution:
    def restoreIpAddresses(self,rawIpString):
     
        def restoreIps(progressIndex, currentSegment, ipAddressSegments):
            
            # If we have filled 4 segments (0, 1, 2, 3) and we are on the 4th, we will only record an answer if the string was decomposed fully
            if currentSegment == 4 and progressIndex == len(rawIpString): restoredIps.append(".".join(ipAddressSegments))
            elif currentSegment == 4:
                return
     
            # Generate segments to try, a segment can be 1 to 3 digits long.
            for segLength in range(1,4):

                if progressIndex + segLength <= len(rawIpString):

                    #Calculate 1 index past where the segment ends index-wise in the original raw ip string
                    onePastSegmentEnd = progressIndex + segLength

                    #Extract int value from our snapshot from the raw ip string
                    segmentAsString = rawIpString[progressIndex:onePastSegmentEnd]
                    segmentValue = int(segmentAsString)

                    # Check the "snapshot's" validity - if invalid break iteration
                    if segmentValue > 255 or segLength >= 2  and segmentAsString[0] == '0': continue
                    
                    # Add the extracted segment to the working segments
                    ipAddressSegments[currentSegment] = segmentAsString

                    #Recurse on the segment choice - when finished & we come back here, the next loop iteration will try another segment
                    restoreIps(progressIndex + segLength, currentSegment + 1, ipAddressSegments)
            
        restoredIps = []
        restoreIps(0, 0, [0]*4)
        return restoredIps




class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        results = []
        def dfs(index, path, sections):
            
            if sections == 4 and index == len(s):
                results.append(path)
                return
            
            elif sections == 4: return
            
            #FOR EACH OF THE POSSIBLE SNIPPETS
            for i in range(1, 4):
                
                if index+i <= len(s):
                    
                    # THE IP SEGMENT WE WILL ADD
                    snippet = s[index:index + i]
                    
                    #THIS WILL CATCH THE 00 OR 01 OR 001 CASES
                    if int(snippet) > 255 or (len(snippet) >= 2 and snippet[0] == '0'): continue
                        
                    dfs(index + i, path + [snippet], sections+1)

        dfs(0,[],0)
        
        return [".".join(ip) for ip in results]


    
class Solution3:
    def restoreIpAddresses(self, s: str):
        
        results = []
        def dfs(startIndex, path, sections):
            
            if sections == 4 and startIndex == len(s): results.append(path)
            elif sections == 4: return
            
            #FOR EACH OF THE POSSIBLE SNIPPETS
            for i in range(1, 4):

                endIndex = startIndex + i

                if endIndex <= len(s):
                    
                    snippet = s[startIndex:endIndex]
                    #THIS WILL CATCH THE 00 OR 01 OR 001 CASES
                    if int(snippet) > 255 or (len(snippet) >= 2 and snippet[0] == '0'): continue
                    dfs(endIndex, path + [snippet], sections+1)

        dfs(0,[],0)
        return [".".join(ip) for ip in results]
                 