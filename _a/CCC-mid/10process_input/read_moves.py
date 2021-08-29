# config number_of_moves black_row black_column white_row white_column etc
# i='a 4 5 6 3 5 7 8 5 6'
i=input().split()
config=i[0]
number_of_moves=int(i[1])
moves=i[2:]

# for j in range(number_of_moves)
#     condition-if-else j%2==0:
#         print('black',j)
#         print(moves[j*2],moves[j*2+1])
#     else:
#         print('white',j)
#         print(moves[j*2],moves[j*2+1])

black_moves=[(moves[j*2],moves[j*2+1]) for j in range(number_of_moves) if j%2==0]
white_moves=[(moves[j*2],moves[j*2+1]) for j in range(number_of_moves) if j%2!=0]

