# Sort words, and save words in list
s="Lundomys molitor, commonly known as the greater marsh rat, is a semiaquatic rat species from southeastern South America."

"""
get words, save to list
sort list
print list
"""

# def toLower(w):
#     return w.lower()

words=s.split()
# words.sort(key=str.lower)
# words=sorted(words,key=str.lower)
# words.sort(key=toLower)
words.sort(key=lambda word: word.lower())
print(words)




