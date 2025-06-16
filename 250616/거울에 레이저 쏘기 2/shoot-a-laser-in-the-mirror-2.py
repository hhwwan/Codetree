n = int(input())
board = [list(input()) for _ in range(n)]
k = int(input())

# 좌표
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

k -= 1
cur_dir = ((k // n) + 1) % 4 # 방향
if cur_dir == 1:
    cr, cc = 0, k % n
elif cur_dir == 2:
    cr, cc = k % n, n - 1
elif cur_dir == 3:
    cr, cc = n - 1, (n - 1) - (k % n)
else:
    cr, cc = (n - 1) - (k % n), 0

# 격자 내 존재 체크
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n
# / 거울일 때 방향전환
def reflect(cur_dir, slash):
    if slash == '/':
        return cur_dir ^ 3
    return cur_dir ^ 1

# 거울상태 체크 후 방향 전환 후 이동
def reflection_move(cur_dir, cr, cc):
    cur_dir = reflect(cur_dir, board[cr][cc])
    nr = cr + dr[cur_dir]
    nc = cc + dc[cur_dir]
    return cur_dir, nr, nc

# 초기방향, 초기좌표
def simulate(cur_dir, cr, cc):
    cnt = 0
    while in_range(cr, cc):
        cur_dir, cr, cc = reflection_move(cur_dir, cr, cc)
        cnt += 1
    return cnt

print(simulate(cur_dir, cr, cc))