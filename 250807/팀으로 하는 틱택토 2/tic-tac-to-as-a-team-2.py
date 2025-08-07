inp = [input() for _ in range(3)]

board = [list(row) for row in inp]

lines = [] # 8개의 줄을 리스트로 저장

# 가로줄
for i in range(3):
    lines.append([board[i][j] for j in range(3)])

# 세로줄
for i in range(3):
    lines.append([board[j][i] for j in range(3)])

# 대각선
lines.append([board[i][i] for i in range(3)])
lines.append([board[i][2 - i] for i in range(3)])

cnt = 0

for line in lines:
    unique_line = set(line)

    if len(unique_line) == 2:
        cnt += 1

print(cnt)