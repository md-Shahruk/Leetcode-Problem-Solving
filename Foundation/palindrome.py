'''
for this problem first we can convert this number to string then we can reverse this string then we can compare normal string vs reverse string.
and return

time: O(n)
space: O(n)

is there any better solution?
we can do:
first extract digit from number %10
shift previous digit to left *10
remove last digit //10 
time: O(log n) because only count digit

'''
def palindrome(s):
    # con_s = str(s)
    # rev  = con_s[::-1]
    # return rev == con_s
    if s < 0:
        return False
    rev = 0
    while s > 0:
        digit = s % 10
        rev = rev * 10 + digit
        s = s // 10
s = -121
print(palindrome(s))