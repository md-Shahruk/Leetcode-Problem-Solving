
def solve(s): 
    vow = {}
    con = {}
    
    for v in s:
        if v in 'aeiou':
            if v in vow:
                vow[v] += 1
            else:
                vow[v] = 1
    for c in s:
        if c not in 'aeiou':
            if c in con:
                con[c] += 1
            else:
                con[c] = 1
    
    max_v = max(vow.values()) if vow else 0
    max_c = max(con.values()) if con else 0
    return max_v + max_c
    return maxx
  

s = "aeiaeia"
print(solve(s))