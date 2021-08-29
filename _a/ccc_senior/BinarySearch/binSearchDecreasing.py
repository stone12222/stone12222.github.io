'''
target = 1
-1, 0, 1, 2, 4, 5, 7, 9, 12
l         m              h
l   m     h
      l(m)h

'''

target = 13
nums = [12, 9, 7, 5, 4, 2, 1, 0, -1]

l = 0
h = len(nums) - 1

while True:
    m = (h+1)//2
    print(l, h, m)

    if l > h:
        print("target at", h, l)
        break

    if target < nums[m]:
        l = m + 1
    elif target > nums[m]:
        h = m - 1
    else:
        print("target at", m)
        break