# A list comprehension is a syntactic construct available
# in some programming languages for creating a list
# based on existing lists.
# It follows the form of the mathematical "set-builder notation"
# (set comprehension)
# https://en.wikipedia.org/wiki/List_comprehension
# -- wiki

# set-builder notation:
# set=[output_expression | variable ∊ input_set, predicate基于]

# List comprehensions can transform one iterable
# (such as list, set, dictionary) into another iterable. 
# with or without conditions

# "What is comprehension?"
# In logic, the comprehension of an object
# is the totality of intensions (内涵)
# including its properties or qualities

l=[1,2,3,4,5,6]

#
l1=[]
for e in l:
    l1.append(e*2)
print(l1)

#
print([e*2 for e in l])

# math set
# https://en.wikipedia.org/wiki/List_comprehension

# [6,8,10,12]
print([e*2 for e in l if e>2])


# 2d
twod=[[(a,b) for a in range(3)] for b in range(3)]

twodd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in twodd for x in row]
print(flat)

# nest comprehension
squared = [[x**2 for x in row] for row in twodd]
print(squared)

