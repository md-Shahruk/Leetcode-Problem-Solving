
def largest_odd(num):

    con_in = int(num)

    if con_in % 2 != 0:
        return num
    else:

        a, b = 0, 0
        if con_in % 2 == 0:
            for i in range(len(num) - 1):
                if int(num[i]) > int(num[i+1]):
                    a = int(num[i])
                else:
                    b = int(num[i+1])
                max_num = max(int(a), int(b))
            if max_num % 2 == 0:
                return ""
            else:
                return str(max_num)
        else:
            return " "

num = "527"
print(largest_odd(num))