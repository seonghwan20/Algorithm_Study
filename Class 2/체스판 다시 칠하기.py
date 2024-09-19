import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

board = [[0 for M in range(M)] for N in range(N)]
modify_list = [[N*M for i in range(M)] for i in range(N)]
for i in range(N):
    board[i] = list(input())

def verify1(lis, x, y, m, n, modify_num):
    if m%2 == 0:
        if n%2 == 0:
            if lis[x][y] != lis[x+m][y+n]:
                modify_num[0] += 1
        elif n%2 != 0:
            if lis[x][y] == lis[x+m][y+n]:
                modify_num[0] += 1
    elif m%2 != 0:
        if n%2 != 0:
            if lis[x][y] != lis[x+m][y+n]:
                modify_num[0] += 1
        elif n%2 == 0:
            if lis[x][y] == lis[x+m][y+n]:
                modify_num[0] += 1

def verify2(lis, x, y, m, n, modify_num):
    if m%2 == 0:
        if n%2 == 0:
            if lis[x][y] != lis[x+m][y+n]:
                modify_num[1] += 1
        elif n%2 != 0:
            if lis[x][y] == lis[x+m][y+n]:
                modify_num[1] += 1
    elif m%2 != 0:
        if n%2 != 0:
            if lis[x][y] != lis[x+m][y+n]:
                modify_num[1] += 1
        elif n%2 == 0:
            if lis[x][y] == lis[x+m][y+n]:
                modify_num[1] += 1
        
for i in range(N):
    if i+7 > N-1:
        break
    for j in range(M):
        if j+7 > M-1:
            break
        modify_num=[0, 1]
        for k in range(8):
            for l in range(8):
                if k==0 and l==0:
                    continue
                verify1(board, i, j, k, l, modify_num)
        if board[i][j] == 'W':
            board[i][j] = 'B'
        else:
            board[i][j]= 'W'
        for k in range(8):
            for l in range(8):
                if k==0 and l==0:
                    continue
                verify2(board, i, j, k, l, modify_num)
        modify_list[i][j] = min(modify_num)
             
min = N*M

for i in range(N):
    for j in range(M):
        if min > modify_list[i][j]:
            min = modify_list[i][j]
print(min)

# import sys

# n, m = map(int, sys.stdin.readline().split())
# org_board = []
# for _ in range(n):
#     org_board.append(sys.stdin.readline().rstrip())

# def w_board_maker(n, m):
#     list = []
#     for i in range(n):
#         raw = ''
#         if i % 2 == 0:
#             for j in range(m):
#                 if j % 2 == 0:
#                     raw += 'W'
#                 else:
#                     raw += 'B'
#         else:
#             for j in range(m):
#                 if j % 2 == 0:
#                     raw += 'B'
#                 else:
#                     raw += 'W'
#         list.append(raw)
#     return list

# def b_board_maker(n, m):
#     list = []
#     for i in range(n):
#         raw = ''
#         if i % 2 == 0:
#             for j in range(m):
#                 if j % 2 == 0:
#                     raw += 'B'
#                 else:
#                     raw += 'W'
#         else:
#             for j in range(m):
#                 if j % 2 == 0:
#                     raw += 'W'
#                 else:
#                     raw += 'B'
#         list.append(raw)
#     return list

# w_chess_board = w_board_maker(n, m)
# b_chess_board = b_board_maker(n, m)

# def checker_maker(n, m):
#     list = []
#     for i in range(n):
#         list.append([0] * m)
#     return list

# w_checker = checker_maker(n, m)
# b_checker = checker_maker(n, m)

# def checker(org_board, board, signal):
#     if signal == 'w':
#         checker = w_checker
#     else:
#         checker = b_checker
#     for raw in range(n):
#         for i in range(m):
#             if org_board[raw][i] == board[raw][i]:
#                 pass
#             else:
#                 checker[raw][i] = 1
#     return checker
  
# w_counter = checker(org_board, w_chess_board, signal='w')
# b_counter = checker(org_board, b_chess_board, signal='b')

# reduced_raws = n - 8
# reduced_columns = m - 8

# def painting_machine(counter):
#     min_counter = n * m
#     for raw in range(reduced_raws+1):
#         for column in range(reduced_columns+1):
#             painting_counter = 0
#             for i in range(8):
#                 painting_counter += sum(counter[raw+i][column:column+8])
#             if min_counter > painting_counter:
#                 min_counter = painting_counter
#     return min_counter

# min_w = painting_machine(w_counter)
# min_b = painting_machine(b_counter)

# print(min(min_b, min_w))