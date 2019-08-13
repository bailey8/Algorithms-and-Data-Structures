def Greedy(input,lengthOfInput):
    for i in range(input):
        x = Select(input)
        if Feasible(x):
            solution = solution + x

def Select