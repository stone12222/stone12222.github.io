k={1:'',
   2:'abc',
   3:'def',
   4:'ghi',
   5:'jkl',
   6:'mno',
   7:'pqrs',
   8:'tuv',
   9:'wxyz'
}

l1=input()
l2=input()

same_bnt=False

for e in k:
    if l1 in k[e] and l2 in k[e]:
        same_bnt=True

if same_bnt:
    print('they are in same button')
else:
    print('they are not in same button')
