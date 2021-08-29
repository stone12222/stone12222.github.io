# in c_in.txt
# the number of phases defined in the first row, each segment end with 0
# in each phase
# condition-if-else there are 3 commands: 1,2,3
# condition-if-else the command is 1, the next line is the number bound with the command 1, it should be saved as (1,number) in the phase
# condition-if-else the command is 2, save (2,) in the phase
# condition-if-else the command is 3, save (3,) in the phase

# print how many phases
# print each phase in each line

f=open('in.txt')
l=[]
for line in f:
    l.append(int(line.strip('\n')))
print(l)

i=0

n_phases=l[i]
phases=[]
for n in range(n_phases):
    i=i+1
    command=l[i]
    p=[]
    while command!=0:
        if command==1:
            i=i+1
            p.append((1, l[i]))
        else:
            p.append((l[i],))
        i=i+1
        command=l[i]
    phases.append(p)

print('there are',len(phases),"phases:")
for p in phases:
    print(p)
