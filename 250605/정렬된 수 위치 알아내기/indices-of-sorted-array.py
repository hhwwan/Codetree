n = int(input())
sequence = list(map(int, input().split()))

# (값, 원래 인덱스) 형태로 저장
indexed_sequence = [(num, idx) for idx, num in enumerate(sequence)]

indexed_sequence.sort(key=lambda x: (x[0], x[1]))

rank = [0] * n

for sorted_idx, (value, original_idx) in enumerate(indexed_sequence, start=1):
    rank[original_idx] = sorted_idx

print(*rank)