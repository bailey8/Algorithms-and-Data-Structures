from collections import defaultdict

# https://leetcode.com/problems/alien-dictionary/discuss/70173/Python-Solution-with-Detailed-Explanation

def alienOrder(self, words):

    # EXTRACT ALL CHARACTERS FROM THE WORDS - THESE ARE THE CHARACTERS WE HAVE TO SORT
    chars = set("".join(words))

    # THIS RECORDS THE NUMBER OF DEGREES
    in_degree = {x: 0 for x in chars}

    # CREATE THE GRAPH
    outgoing_edges = defaultdict(list)

    # THIS MATCHES EACH WORD NEXT TO THE WORD BEHIND IT IN THE DIC { (WORD1,WORD2),(WORD2,WORD3)... (WORD_N-1, WORD_N)}
    for pair in zip(words, words[1:]):
        #EXAMPLE PAIR: ("WORD1","WORD2") - IT JUST ITERATES OVER THE TUPLES
        #THIS GOES CHARACTER BY CHARACTER OF THE 2 WORDS IN THE TUPLE "W" AND "W" THEN "O" AND "O"
        for word1Char, word2Char in zip(*pair):
            #IF THE FIRST LETTERS DONT MATCH IN THE WORDS
            if word1Char != word2Char:

                #ADD AN EDGE FROM CHAR1 TO CHAR2
                outgoing_edges[word1Char].append(word2Char)
                # INCREMENT THE NUMBER OF INCOMING EDGES FOR CHAR2
                in_degree[word2Char] += 1

            #  The first non-matching character determines a relationship u -> v and is added to outgoing_edges.
            #  We break at this point since the remainder mis-matches do not imply any relationship.   
                break

    # THE LIST OF LETTERS WITH NO INCOMING EDGES
    queue = [node for node in in_degree if in_degree[node] == 0]
    # OUR RESPONSE SET
    properOrder = str()

    # THIS IS KHANS ALGO
    while queue:
        character = queue.pop()
        # ADD THE LETTER TO THE QUEUE (THIS IS THE TOPSORT ARRAY IN KHANS)
        properOrder += character

        #FOR ALL OUTGOING EDGES, DECREMENT THE INDEGREE BC WE JUST PROCESSED ONE OF THEIR PREREQS
        for child in outgoing_edges[character]:
            degrees[child] -= 1
            # IF THE CHARACTER HAS NO MORE PREREQS
            if in_degree[child] == 0:
                queue.append(child)

    return properOrder if len(set(properOrder)) == len(chars) else ""

class Solution5:
    def alienOrder(self, words):

        characterSet = set("".join(words))
        outgoing  = collections.defaultdict(list)
        inDegree = {char:0 for char in characterSet}


        # Make the edges we know are present
        for word in zip(words,words[1:]):
            for leftChar, rightChar in zip(*word):
                if leftChar != rightChar:
                    outgoing[leftChar].append(rightChar)
                    inDegree[rightChar] += 1
                    break


        stack = [char for char in inDegree if inDegree[char] == 0]
        topologicalOrder = []

        while stack:

            root = stack.pop()
            topologicalOrder.append(root)
            
            for neigh in outgoing[root]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    stack.append(neigh)

        return "".join(topologicalOrder) if len(topologicalOrder) == len(characterSet) else ""


a = set("word")
a.add("hi")
print(a)

w1 = [
    "WORD1",
    "word2",
    "word3",
    "word4",
    "word5"
]


# for pair in (zip(w1, w1[1:])):
#     for x, y in zip(*pair):
#         print(x,y)

print( 2 == True)