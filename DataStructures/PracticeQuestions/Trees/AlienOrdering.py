from collections import defaultdict

def alienOrder(self, words):
    chars = set("".join(words))
    degrees = {x:0 for x in chars}
    graph = defaultdict(list)
    # get tuples of words
    for pair in zip(words, words[1:]):
        # Since words may be different letter, unpack the tuple, then zip again to make sure words are same length
        for x, y in zip(*pair):
            if x != y:
                graph[x].append(y)
                degrees[y] += 1
                break
                
    queue = filter(lambda x: degrees[x] == 0, degrees.keys())
    ret = ""
    while queue:
        x = queue.pop()
        ret += x
        for n in graph[x]:
            degrees[n] -= 1
            if degrees[n] == 0:
                queue.append(n)
           
    # https://leetcode.com/problems/alien-dictionary/discuss/70173/Python-Solution-with-Detailed-Explanation
    return ret * (set(ret) == chars)

