
def split_balanced(s):
    b = 0
    c = 0
    for char in s:
        if char == "R":
            b += 1
        else:
            b -= 1
        if b == 0:
            c += 1
    return c 

             
s = "RLRRLLRLRL"

print(split_balanced(s))