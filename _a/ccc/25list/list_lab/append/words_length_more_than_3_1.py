"""
split a sentence to a list of words
find out the number of words whose length
are more than 3
print the number
print those words
"""
s='Teens Programming is the 1st London-based, ' \
  'industry-level, year-round, dedicated computer ' \
  'programming school for kids, teens and youth ' \
  'in London Ontario.'

words=s.split()
numOfNodes=0
r=[]

for w in words:
    if len(w)>3:
        numOfNodes+=1
        r.append(w)

print(numOfNodes)
print(r)



