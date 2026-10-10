def last_word_len(s):
    # trim_text = " ".join(s.split())
    # last_word = trim_text.split()[-1]
    
    # return len(last_word)
    i = len(s) - 1
    l = 0
    
    while i > 0 and s[i] == ' ':
        i -= 1
    while i > 0 and s[i]!= ' ':
        l += 1
        i -= 1
    return l  


s = " Hello world "
print(last_word_len(s))