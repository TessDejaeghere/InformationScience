import string 

with open("corpus.txt", 'r') as corpus:
        text = corpus.read().split()

nopunc = []
for word in text: 
    word = word.lower()
    word = word.translate(str.maketrans("", "", string.punctuation))
    nopunc.append(word)
    
freq = {}    
for x in nopunc: 
    if x in freq:
        freq[x] += 1
    else: 
        freq[x] = 1

sorted_x = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_x)