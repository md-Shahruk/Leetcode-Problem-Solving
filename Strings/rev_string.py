
def rev_string(s,k):

    if len(s) < k:
        return s[::-1]
    else:
        res = []
        i = 0
        rev = True
        while i < len(s):
            chu = s[i:i+k]
            if rev:
                chu = chu[::-1]
            res.append(chu)
            i += k
            rev = not rev 
        return "".join(res)
           



s = "abcd"
k = 6

print(rev_string(s,k))