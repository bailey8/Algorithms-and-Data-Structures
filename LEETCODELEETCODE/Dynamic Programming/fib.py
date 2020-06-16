def fib(N):
    if N<=1:
        return N
    return fib(N-1) + fib(N-2)

print(fib(4))

mem = {}
def memoized_fib(N):
    if N <= 1:
        return N
    if N-1 not in mem: mem[N-1] = memoized_fib(N-1)
    if N-2 not in mem: mem[N-2] = memoized_fib(N-2)
    return mem[N-1] + mem[N-2]
print(memoized_fib(4))

def memoized_fib2(N,mem):
    if N <= 1:
        return N
    if N-1 not in mem: mem[N-1] = memoized_fib2(N-1,mem)
    if N-2 not in mem: mem[N-2] = memoized_fib2(N-2,mem)
    return mem[N-1] + mem[N-2]

print(memoized_fib2(4,{}))

def bottum_up(N):
    if N <= 1:
        return N
    results = [0] *(N+1)
    results[1] = 1
    for i in range(2,N+1):
        results[i] = results[i-1] + results[i-2]
    return results[N]

print(bottum_up(4))