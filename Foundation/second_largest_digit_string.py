'''
for this problem we can check in a stirng is it number or char?
if it is number then this string number convert to number.

then go for compare with a and b and store second largest to b and return
Time: O(n)
Space: O(1)
'''

def secondLargest(s):
    a, b = -1, -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if num > a:
                b = a 
                a = num 
            elif num < a and num > b:
                b = num 
    return b 
        
    

s = "sjhtz8344"
print(secondLargest(s))