
def largest_odd(num):

    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i+1]

      
   
num = "527"
print(largest_odd(num))