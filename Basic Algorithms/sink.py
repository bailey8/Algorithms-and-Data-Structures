Input: A (adj Matrix)

initialize a set named candidates

for node in A[0]:
    add node to candidates

while sizeOf(candidates) > 1:
    # i is incremented by 2 each time to process each pair
    for(int i = 0; i < sizeOf(candidates)-1 ; i = i+2)
        node1 = candidates[i]
        node2 = candidates[i+1]
        if A[node1][node2] == 0:
            remove node2 from candidates
        else:
            remove node1 from candidates
        i += 2

# At this point there is only 1 node in candidates,
# So pass it into the algo from part A to determine if its a sink
return AlgoFromPartA(candidates[0])
     