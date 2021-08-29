# Sort string list
s="in December 1989 I was looking for a hobby programming project that would keep me occupied during the week around Christmas"
s_list=s.split()
s_list.sort(key=lambda s:s.lower())
print(s_list)

s1_list=s.split()
def valueToSort(el):
    return el.lower()

s1_list.sort(key=valueToSort)
print(s1_list)

# or
# key is a function that receives a element and return a value that will be used for sort
s="in December 1989 I was looking for a hobby programming project that would keep me occupied during the week around Christmas"
new_s=sorted(s.split(),key=str.lower)
print(new_s)
