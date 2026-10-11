
def solve(jewels, stones):
    j_set = set(jewels)
    c = 0
    
    for s in stones:
        if s in j_set:
            c += 1
    return c

jewels = "aAC"
stones = "aAAbbbbC"

print(solve(jewels, stones))