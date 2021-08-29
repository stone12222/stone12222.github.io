# remove number
# >2, <7
# print li

li=[1,2,3,4,5,6,7]
for e in li:
    if e>2 and e<7:
        # print(e,"removed")
        li.remove(e)
print(li)

