
## Find words containing character

def find_word_char(words, x):
    
    store_index = []
    for i in range(len(words)):
            if x in words[i]:
                store_index.append(i)
    return store_index
    

words =  ["abc","bcd","aaaa","cbc"]
x = "a"
print(find_word_char(words, x))