'''
target = 1
-1, 0, 1, 2, 4, 5, 7, 9, 12
l         m              h
l   m     h
      l(m)h

'''

target = 1
nums = [-1, 0, 1, 2, 4, 5, 7, 9, 12]

l = 0
h = len(nums) - 1

while True:
    m = (h+1)//2
    print(l, h, m)

    if target < nums[m]:
        h = m-1
    elif target > nums[m]:
        l = m+1
    else:
        print("target at", m)
        break