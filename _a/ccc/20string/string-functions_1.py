# len=length
str1="hello"
print(len(str1))

#
lines="""
    line
    line
    line
"""
print(lines.split())
print(lines.splitlines(keepends=True))
print(lines.splitlines(True))

# delete chars by using replace
str1="abcdefg"
str2=str1.replace("abc","")
print(str2)

# dir
str_properties=dir(str1)
print(str_properties)



